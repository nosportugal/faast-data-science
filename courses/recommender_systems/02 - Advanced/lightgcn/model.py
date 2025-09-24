"""
Minimal LightGCN-style model with sparse propagation.

- Initializes embeddings for all nodes (users+items) in one table.
- Propagates K hops via normalized adjacency (sparse mm).
- Returns final embeddings as layer-wise mean.
"""
from __future__ import annotations

from typing import Optional

import torch
import torch.nn as nn


class LightGCNSimple(nn.Module):
    """
    Minimal, readable LightGCN-style model with Step 1 upgrades:
    - Optional learnable layer weights (alpha) with softmax normalization.
    - Edge dropout (a.k.a. message dropout) applied to adjacency during training.

    Args:
        num_nodes: Total nodes (num_users + num_items).
        embed_dim: Embedding dimensionality.
        num_layers: Number of propagation steps (K).
        alpha_mode: "mean" (default) for equal layer weights, or "learnable" for softmax(alpha_k).
        edge_dropout: Probability of dropping an edge weight during propagation (0.0 disables).
        device: Optional torch.device.
    """

    def __init__(
        self,
        num_nodes: int,
        embed_dim: int = 64,
        num_layers: int = 3,
        alpha_mode: str = "mean",  # "mean" | "learnable"
        edge_dropout: float = 0.0,
        device: Optional[torch.device] = None,
    ):
        super().__init__()
        assert num_layers >= 0
        assert alpha_mode in {"mean", "learnable"}
        assert 0.0 <= edge_dropout < 1.0

        self.num_nodes = num_nodes
        self.embed_dim = embed_dim
        self.num_layers = num_layers
        self.alpha_mode = alpha_mode
        self.edge_dropout = float(edge_dropout)

        self.E = nn.Embedding(num_nodes, embed_dim)
        nn.init.normal_(self.E.weight, std=0.1)

        if self.alpha_mode == "learnable":
            # K+1 weights to combine layers 0..K
            self.alpha = nn.Parameter(torch.zeros(
                num_layers + 1, dtype=torch.float32))
        else:
            self.register_parameter("alpha", None)

        self.device = device
        if device is not None:
            self.to(device)

    @staticmethod
    def _dropout_sparse(A: torch.Tensor, p: float) -> torch.Tensor:
        """
        Apply dropout on non-zero values of a sparse adjacency A.
        Scale by 1/(1-p) to keep expected sum unchanged.
        """
        if p <= 0.0:
            return A
        A = A.coalesce()
        idx = A.indices()
        val = A.values()
        keep = torch.rand_like(val) > p
        if keep.sum() == 0:
            return A  # avoid empty adjacency
        val = val * keep.float() / (1.0 - p)
        return torch.sparse_coo_tensor(idx, val, A.shape, device=A.device).coalesce()

    def propagate(self, A_norm: torch.Tensor, training: bool = True) -> torch.Tensor:
        """
        Perform K-hop propagation and combine layer embeddings.

        Args:
            A_norm: Coalesced sparse adjacency tensor (N x N).
            training: Whether called under training (controls edge dropout).
        Returns:
            Z: Combined node embeddings (N x d).
        """
        x = self.E.weight
        xs = [x]

        for _ in range(self.num_layers):
            A_cur = self._dropout_sparse(
                A_norm, self.edge_dropout) if training and self.edge_dropout > 0 else A_norm
            x = torch.sparse.mm(A_cur, x)
            xs.append(x)

        stack = torch.stack(xs, dim=0)  # (K+1, N, d)

        if self.alpha_mode == "mean":
            Z = stack.mean(dim=0)
        else:
            # Learnable alphas -> softmax over layers
            w = torch.softmax(self.alpha, dim=0).view(-1, 1, 1)  # (K+1, 1, 1)
            Z = (stack * w).sum(dim=0)
        return Z

    def forward(self, A_norm: torch.Tensor, training: bool = True) -> torch.Tensor:
        return self.propagate(A_norm, training=training)