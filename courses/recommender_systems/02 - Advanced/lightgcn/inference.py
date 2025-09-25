from __future__ import annotations

from typing import Dict, List, Optional, Tuple, Iterable

import numpy as np
import pandas as pd
import torch


def l2_normalize(X: torch.Tensor, eps: float = 1e-12) -> torch.Tensor:
    """Row-wise L2 normalization (safe)."""
    norms = torch.norm(X, p=2, dim=1, keepdim=True).clamp_min(eps)
    return X / norms


def recommend_for_user_topk(
    user_raw_id: int,
    U_emb: torch.Tensor,
    I_emb: torch.Tensor,
    u2idx: Dict[int, int],
    idx2i: List[int],
    topk: int = 10,
    exclude_seen: bool = True,
    user_pos_raw: Optional[Dict[int, set]] = None,
) -> List[Tuple[int, float]]:
    """
    Recommend top-K items for a user via dot-product scoring.

    Args:
        user_raw_id: MovieLens userId
        U_emb: (U, d) tensor
        I_emb: (I, d) tensor
        u2idx: raw userId -> contiguous index
        idx2i: contiguous item index -> raw movieId
        topk: number of items to return
        exclude_seen: filter previously interacted items
        user_pos_raw: optional dict raw userId -> set of raw movieIds

    Returns:
        List of (movieId, score) sorted by score desc.
    """
    u_idx = u2idx[user_raw_id]
    u_vec = U_emb[u_idx:u_idx + 1]  # (1, d)
    scores = (u_vec @ I_emb.T).squeeze(0).detach().cpu().numpy()

    if exclude_seen and user_pos_raw is not None:
        seen = user_pos_raw.get(user_raw_id, set())
        # Map raw -> contiguous indices
        seen_idx = [i for i, mid in enumerate(idx2i) if mid in seen]
        if seen_idx:
            scores[np.array(seen_idx, dtype=np.int64)] = -np.inf

    k = min(topk, len(scores))
    top_idx = np.argpartition(-scores, range(k))[:k]
    top_idx = top_idx[np.argsort(-scores[top_idx])]
    return [(idx2i[j], float(scores[j])) for j in top_idx]


def similar_items_by_title(
    query: str,
    I_emb: torch.Tensor,
    movies_df: pd.DataFrame,
    idx2i: List[int],
    i2idx: Dict[int, int],
    topk: int = 10,
    normalize: bool = True,
) -> List[Tuple[int, str, float]]:
    """
    Find top-K similar items to a movie title (substring match).

    Args:
        query: title substring (case-insensitive)
        I_emb: (I, d) item embeddings
        movies_df: DataFrame with columns ['movieId','title']
        idx2i: contiguous item index -> raw movieId
        i2idx: raw movieId -> contiguous item index
        topk: number of similar items
        normalize: if True, cosine sim; else dot product

    Returns:
        List of (movieId, title, similarity) including the query at rank 1.
    """
    m = movies_df[movies_df["title"].str.contains(query, case=False, na=False)]
    if m.empty:
        return []
    # Pick first match by default
    mid = int(m.iloc[0]["movieId"])
    if mid not in i2idx:
        return []

    q_idx = i2idx[mid]
    Q = I_emb
    if normalize:
        Q = l2_normalize(Q)

    q_vec = Q[q_idx:q_idx + 1]  # (1, d)
    sims = (q_vec @ Q.T).squeeze(0).detach().cpu().numpy()

    k = min(topk, len(sims))
    top_idx = np.argpartition(-sims, range(k))[:k]
    top_idx = top_idx[np.argsort(-sims[top_idx])]

    id_to_title = dict(zip(movies_df["movieId"], movies_df["title"]))
    out: List[Tuple[int, str, float]] = []
    for idx in top_idx:
        movie_id = idx2i[idx]
        title = id_to_title.get(movie_id, str(movie_id))
        out.append((movie_id, title, float(sims[idx])))
    return out


def write_topk_csv(
    out_path: str,
    user_ids: Iterable[int],
    U_emb: torch.Tensor,
    I_emb: torch.Tensor,
    u2idx: Dict[int, int],
    idx2i: List[int],
    topk: int,
    exclude_seen: bool = True,
    user_pos_raw: Optional[Dict[int, set]] = None,
) -> None:
    """
    Write predictions CSV compatible with BLU12 evaluation:
    column0=user_id, columns1..K=item_ids, no header.
    """
    rows = []
    for uid in user_ids:
        recs = recommend_for_user_topk(
            user_raw_id=uid,
            U_emb=U_emb,
            I_emb=I_emb,
            u2idx=u2idx,
            idx2i=idx2i,
            topk=topk,
            exclude_seen=exclude_seen,
            user_pos_raw=user_pos_raw,
        )
        rows.append([uid] + [mid for mid, _ in recs])
    pd.DataFrame(rows).to_csv(out_path, index=False, header=False)
