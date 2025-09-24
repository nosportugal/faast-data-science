"""
Utility helpers for LightGCN training and evaluation.
"""
from __future__ import annotations

from typing import Dict, Set, Tuple, Optional

import numpy as np
import torch
from scipy import sparse


def scipy_to_torch_sparse(mat: sparse.spmatrix, device: Optional[torch.device] = None) -> torch.Tensor:
    """Convert a SciPy sparse matrix to a coalesced PyTorch sparse COO tensor."""
    mat = mat.tocoo()
    indices = torch.tensor(
        np.vstack((mat.row, mat.col)),
        dtype=torch.long,
        # cpu tensor for indices on MPS
        device=device if device and device.type != "mps" else None,
    )
    values = torch.tensor(mat.data, dtype=torch.float32, device=device)
    shape = torch.Size(mat.shape)
    return torch.sparse_coo_tensor(indices, values, shape).coalesce().to(device) if device else \
        torch.sparse_coo_tensor(indices, values, shape).coalesce()


def build_norm_adj_from_R(R: sparse.csr_matrix) -> sparse.csr_matrix:
    """
    Build symmetric normalized adjacency A_norm = D^{-1/2} A D^{-1/2}
    from a user-item interaction matrix R (U x I).

        A = [[0,   R ],
             [R^T, 0 ]]

    Returns:
        A_norm as CSR (shape (U+I, U+I))
    """
    U, I = R.shape
    zero_U = sparse.csr_matrix((U, U))
    zero_I = sparse.csr_matrix((I, I))
    upper = sparse.hstack([zero_U, R], format="csr")
    lower = sparse.hstack([R.T, zero_I], format="csr")
    A = sparse.vstack([upper, lower], format="csr")

    deg = np.asarray(A.sum(axis=1)).ravel()
    d_inv_sqrt = 1.0 / np.sqrt(np.clip(deg, 1e-12, None))
    D_inv_sqrt = sparse.diags(d_inv_sqrt)
    A_norm = (D_inv_sqrt @ A @ D_inv_sqrt).tocsr()
    return A_norm


def bpr_loss(u_e: torch.Tensor, pos_e: torch.Tensor, neg_e: torch.Tensor, reg: float = 1e-4) -> torch.Tensor:
    """Bayesian Personalized Ranking loss with simple L2 regularization on embeddings."""
    pos_scores = (u_e * pos_e).sum(dim=1)
    neg_scores = (u_e * neg_e).sum(dim=1)
    loss = -torch.nn.functional.logsigmoid(pos_scores - neg_scores).mean()
    if reg > 0:
        loss = loss + reg * (u_e.pow(2).mean() +
                             pos_e.pow(2).mean() + neg_e.pow(2).mean())
    return loss


def sample_bpr_triples(
    user_pos: Dict[int, Set[int]],
    num_users: int,
    num_items: int,
    batch_size: int,
    neg_sampling: str = "uniform",  # "uniform" | "popularity"
    item_pop: Optional[np.ndarray] = None,
    rng: Optional[np.random.Generator] = None,
) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """
    Sample a batch of (user_idx, pos_item_idx, neg_item_idx) triples.

    - Positive sampled uniformly from the user's positives.
    - Negative sampled either uniformly from unobserved items, or
      proportionally to item popularity (popularity-aware).
    """
    assert neg_sampling in {"uniform", "popularity"}
    rng = rng or np.random.default_rng()

    users = rng.integers(low=0, high=num_users,
                         size=batch_size, endpoint=False)
    pos = np.empty(batch_size, dtype=np.int64)
    neg = np.empty(batch_size, dtype=np.int64)

    # Precompute popularity probabilities if needed
    if neg_sampling == "popularity":
        if item_pop is None:
            raise ValueError(
                "item_pop must be provided for popularity-aware sampling.")
        probs = item_pop.astype(np.float64)
        if probs.sum() == 0:
            probs = np.ones_like(probs)  # fallback to uniform
        probs = probs / probs.sum()

    for idx, u in enumerate(users):
        pos_set = user_pos.get(u, None)
        if not pos_set:
            # Fallback: if a user has no positives (unlikely), skip to random item
            pos[idx] = rng.integers(0, num_items)
        else:
            # Sample a positive uniformly
            pos[idx] = rng.choice(list(pos_set))

        # Sample a negative
        tries = 0
        while True:
            if neg_sampling == "uniform":
                j = int(rng.integers(0, num_items))
            else:
                j = int(rng.choice(num_items, p=probs))
            if pos_set is None or j not in pos_set or tries > 10:
                neg[idx] = j
                break
            tries += 1

    u_idx = torch.from_numpy(users).long()
    p_idx = torch.from_numpy(pos).long()
    n_idx = torch.from_numpy(neg).long()
    return u_idx, p_idx, n_idx


def recommend_for_user(
    user_idx: int,
    Z: torch.Tensor,
    n_users: int,
    topk: int = 10,
    exclude: Iterable[int] | None = None,
) -> List[int]:
    """Recommend top-k item indices for a user given final embeddings Z."""
    U_emb = Z[:n_users]
    I_emb = Z[n_users:]
    u = U_emb[user_idx: user_idx + 1]
    scores = (u @ I_emb.T).squeeze(0).detach().cpu().numpy()
    if exclude:
        for i in exclude:
            if 0 <= i < len(scores):
                scores[i] = -np.inf
    top_idx = np.argpartition(-scores, range(min(topk, len(scores))))[:topk]
    top_idx = top_idx[np.argsort(-scores[top_idx])]
    return top_idx.tolist()
