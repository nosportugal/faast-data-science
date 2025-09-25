"""
LightGCN dataset builder for MovieLens 20M (ml-20m).

This module prepares a bipartite user-item graph from implicit feedback
(rating >= threshold). It returns:
- mappings between raw ids and contiguous indices
- a SciPy CSR user-item matrix
- a normalized symmetric adjacency matrix A_norm (D^{-1/2} A D^{-1/2})

Paths are resolved relative to the repo root. Default expects data at
./data/ml-20m/{ratings.csv,movies.csv}.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Dict, List, Tuple, Set, Optional

import numpy as np
import pandas as pd
from scipy import sparse


@dataclass
class GraphData:
    """Container holding graph/data artifacts for LightGCN training."""
    num_users: int
    num_items: int
    R: sparse.csr_matrix  # User-Item implicit interactions (U x I)
    u2idx: Dict[int, int]
    i2idx: Dict[int, int]
    idx2u: List[int]
    idx2i: List[int]
    user_pos: Dict[int, Set[int]]  # user_idx -> set(item_idx)
    item_pop: np.ndarray  # shape (num_items,), interaction counts per item


def load_ml20m_graph(
    data_root: str,
    min_rating: float = 4.0,
    limit_users: Optional[int] = None,
    limit_items: Optional[int] = None,
) -> GraphData:
    """
    Load MovieLens 20M ratings and build an implicit user-item graph.

    - Keeps ratings >= min_rating as positive interactions.
    - Maps raw IDs to contiguous indices.
    - Builds sparse CSR R (U x I), user_pos sets, and item popularity counts.

    Args:
        data_root: Path to ml-20m folder (contains ratings.csv, movies.csv, ...).
        min_rating: Minimum rating to consider an interaction positive.
        limit_users: If provided, only use the first N unique users (for quick runs).
        limit_items: If provided, only use the first M unique items.

    Returns:
        GraphData with all artifacts needed downstream.
    """
    ratings_fp = os.path.join(data_root, "ratings.csv")
    if not os.path.exists(ratings_fp):
        raise FileNotFoundError(f"Could not find ratings.csv at: {ratings_fp}")

    usecols = ["userId", "movieId", "rating"]
    ratings = pd.read_csv(ratings_fp, usecols=usecols)
    pos = ratings[ratings["rating"] >= min_rating].copy()

    # Optional: limit users/items (first N by sorted ID) for quicker experiments.
    if limit_users is not None:
        sel_users = sorted(pos["userId"].unique())[: int(limit_users)]
        pos = pos[pos["userId"].isin(sel_users)]
    if limit_items is not None:
        sel_items = sorted(pos["movieId"].unique())[: int(limit_items)]
        pos = pos[pos["movieId"].isin(sel_items)]

    u_raw = sorted(pos["userId"].unique())
    i_raw = sorted(pos["movieId"].unique())
    u2idx = {u: i for i, u in enumerate(u_raw)}
    i2idx = {m: j for j, m in enumerate(i_raw)}
    idx2u = u_raw
    idx2i = i_raw

    rows = np.fromiter(
        (u2idx[u] for u in pos["userId"].values), dtype=np.int64, count=len(pos))
    cols = np.fromiter(
        (i2idx[m] for m in pos["movieId"].values), dtype=np.int64, count=len(pos))
    data = np.ones(len(pos), dtype=np.float32)

    U, I = len(u_raw), len(i_raw)
    R = sparse.coo_matrix((data, (rows, cols)), shape=(U, I)).tocsr()

    # user -> positives and item popularity
    user_pos: Dict[int, Set[int]] = {}
    R_csr = R.tocsr()
    for u in range(U):
        start, end = R_csr.indptr[u], R_csr.indptr[u + 1]
        user_pos[u] = set(R_csr.indices[start:end])

    item_pop = np.asarray(R.sum(axis=0)).ravel().astype(np.float64)  # (I,)

    return GraphData(
        num_users=U,
        num_items=I,
        R=R,
        u2idx=u2idx,
        i2idx=i2idx,
        idx2u=idx2u,
        idx2i=idx2i,
        user_pos=user_pos,
        item_pop=item_pop,
    )
