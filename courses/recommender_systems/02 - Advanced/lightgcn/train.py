"""
End-to-end training script for LightGCN on MovieLens 20M.

Outputs:
- Saves a .pt file with final node embeddings (users+items) and id maps.
- Prints tiny sample recommendations for sanity check.

Run from repo root or from this folder. Adjust paths via CLI args or defaults.
"""
from __future__ import annotations

import argparse
import json
import os
from typing import Dict, Any

import numpy as np
import torch
from torch.optim import Adam

from dataset import load_ml20m_graph
from model import LightGCNSimple
from utils import build_norm_adj_from_R, scipy_to_torch_sparse, bpr_loss, sample_bpr_triples


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Train LightGCN on MovieLens 20M and save embeddings.")
    p.add_argument("--data-root", type=str,
                   default="./data/ml-20m", help="Path to ml-20m folder.")
    p.add_argument("--min-rating", type=float, default=4.0,
                   help="Minimum rating for implicit positive.")
    p.add_argument("--limit-users", type=int, default=None,
                   help="Optional: limit number of users (quick runs).")
    p.add_argument("--limit-items", type=int, default=None,
                   help="Optional: limit number of items (quick runs).")

    p.add_argument("--embed-dim", type=int, default=64)
    p.add_argument("--layers", type=int, default=3)
    p.add_argument("--alpha-mode", type=str, default="mean",
                   choices=["mean", "learnable"])
    p.add_argument("--edge-dropout", type=float, default=0.0)

    p.add_argument("--epochs", type=int, default=3)
    p.add_argument("--batch-size", type=int, default=4096)
    p.add_argument("--steps-per-epoch", type=int, default=500,
                   help="Batches per epoch (approx).")
    p.add_argument("--lr", type=float, default=1e-2)
    p.add_argument("--weight-decay", type=float, default=1e-6)
    p.add_argument("--neg-sampling", type=str, default="uniform",
                   choices=["uniform", "popularity"])

    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--device", type=str, default="cpu",
                   choices=["auto", "cpu", "cuda", "mps"])
    p.add_argument("--out", type=str, default="./data/lightgcn_ml20m_embeddings.pt",
                   help="Output path for saved embeddings/checkpoint.")

    return p.parse_args()


def choose_device(pref: str) -> torch.device:
    if pref == "cpu":
        return torch.device("cpu")
    if pref == "cuda" and torch.cuda.is_available():
        return torch.device("cuda")
    if pref == "mps" and torch.backends.mps.is_available():
        return torch.device("mps")
    if pref == "auto":
        if torch.cuda.is_available():
            return torch.device("cuda")
        if torch.backends.mps.is_available():
            return torch.device("mps")
    return torch.device("cpu")


def main() -> None:
    args = parse_args()

    # Repro
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    device = choose_device(args.device)
    print(f"Using device: {device}")

    # Load data
    print("Loading MovieLens 20M and building graph...")
    g = load_ml20m_graph(
        data_root=args.data_root,
        min_rating=args.min_rating,
        limit_users=args.limit_users,
        limit_items=args.limit_items,
    )
    U, I = g.num_users, g.num_items
    print(f"Users: {U}, Items: {I}, Interactions: {g.R.nnz}")

    # Build normalized adjacency and convert to torch sparse
    A_norm = build_norm_adj_from_R(g.R)
    A_norm_t = scipy_to_torch_sparse(A_norm, device=device)

    # Model
    model = LightGCNSimple(
        num_nodes=U + I,
        embed_dim=args.embed_dim,
        num_layers=args.layers,
        alpha_mode=args.alpha_mode,
        edge_dropout=args.edge_dropout,
        device=device,
    )
    print(model)

    opt = Adam(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)

    rng = np.random.default_rng(args.seed)

    # Training
    for ep in range(1, args.epochs + 1):
        model.train()
        running = 0.0

        for step in range(1, args.steps_per_epoch + 1):
            # Sample BPR triples
            u_idx, p_idx, n_idx = sample_bpr_triples(
                user_pos=g.user_pos,
                num_users=U,
                num_items=I,
                batch_size=args.batch_size,
                neg_sampling=args.neg_sampling,
                item_pop=g.item_pop,
                rng=rng,
            )

            u_idx = u_idx.to(device)
            p_idx = p_idx.to(device)
            n_idx = n_idx.to(device)

            # Forward (propagate) – we recompute per step for correct gradients.
            Z = model(A_norm_t, training=True)  # (U+I, d)
            U_emb = Z[:U]
            I_emb = Z[U:]

            loss = bpr_loss(U_emb[u_idx], I_emb[p_idx],
                            I_emb[n_idx], reg=args.weight_decay)

            opt.zero_grad()
            loss.backward()
            opt.step()

            running += float(loss.detach().cpu())
            if step % 50 == 0:
                print(f"Epoch {ep}/{args.epochs} - Step {step}/{args.steps_per_epoch} - "
                      f"BPR loss: {running/50:.4f}")
                running = 0.0

        # End of epoch summary
        print(f"Epoch {ep} completed.")

    # Save final embeddings
    model.eval()
    with torch.no_grad():
        Z = model(A_norm_t, training=False).detach().cpu()
        E0 = model.E.weight.detach().cpu()

    payload: Dict[str, Any] = {
        "config": {
            "embed_dim": args.embed_dim,
            "layers": args.layers,
            "alpha_mode": args.alpha_mode,
            "edge_dropout": args.edge_dropout,
            "min_rating": args.min_rating,
            "neg_sampling": args.neg_sampling,
        },
        "num_users": U,
        "num_items": I,
        "idx2u": g.idx2u,
        "idx2i": g.idx2i,
        "u2idx": g.u2idx,
        "i2idx": g.i2idx,
        "E0": E0,  # base embeddings
        "Z": Z,    # propagated embeddings
    }

    out_dir = os.path.dirname(os.path.abspath(args.out))
    os.makedirs(out_dir, exist_ok=True)
    torch.save(payload, args.out)
    print(f"Saved embeddings and mappings to: {args.out}")

    # Also write a small JSON sidecar with shapes and config for quick inspection.
    meta = {
        "num_users": U,
        "num_items": I,
        "embed_dim": args.embed_dim,
        "layers": args.layers,
        "alpha_mode": args.alpha_mode,
        "edge_dropout": args.edge_dropout,
        "out_file": os.path.abspath(args.out),
    }
    try:
        with open(os.path.splitext(args.out)[0] + ".json", "w") as f:
            json.dump(meta, f, indent=2)
        print("Wrote metadata JSON.")
    except Exception as e:
        print("Warning: failed to write metadata JSON:", e)


if __name__ == "__main__":
    main()
