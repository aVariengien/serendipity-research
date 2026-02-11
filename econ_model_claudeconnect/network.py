"""
Network generation for the social network simulation.

Generates realistic social networks with heterogeneous (power-law) degree
distributions while avoiding unnatural chain-heavy artifacts.

Small networks (n < 15) use Barabasi-Albert preferential attachment.
Larger networks use a dual Barabasi-Albert model (mix of low/high attachment)
plus a light triadic-closure pass for local clustering.
"""

import numpy as np
import networkx as nx


def _add_triadic_closure(
    G: nx.Graph, rng: np.random.Generator, triad_prob: float = 0.15
) -> nx.Graph:
    """Add light friend-of-friend closure to increase local clustering."""
    for u in list(G.nodes()):
        neighbors = list(G.neighbors(u))
        if len(neighbors) < 2:
            continue
        # Add a few potential neighbor-neighbor links per node.
        attempts = min(3, len(neighbors) // 2)
        for _ in range(attempts):
            if rng.random() >= triad_prob:
                continue
            a, b = rng.choice(neighbors, size=2, replace=False)
            if a != b:
                G.add_edge(int(a), int(b))
    return G


def _ensure_connected(G: nx.Graph, rng: np.random.Generator) -> nx.Graph:
    """If the graph has multiple components, connect them by adding edges."""
    components = list(nx.connected_components(G))
    if len(components) <= 1:
        return G

    # Connect each component to the next by adding an edge
    for i in range(len(components) - 1):
        u = rng.choice(list(components[i]))
        v = rng.choice(list(components[i + 1]))
        G.add_edge(u, v)

    return G


def generate_network(n: int, seed: int | None = None) -> nx.Graph:
    """Generate a social network with n users and a power-law degree distribution.

    Parameters
    ----------
    n : int
        Number of users (nodes).
    seed : int or None
        Random seed for reproducibility.

    Returns
    -------
    nx.Graph
        An undirected, connected graph with n nodes (labeled 0..n-1).
    """
    rng = np.random.default_rng(seed)
    nx_seed = int(rng.integers(0, 2**31))

    if n < 3:
        # Trivial case: complete graph
        G = nx.complete_graph(n)
    elif n < 15:
        # Small network: simple preferential attachment.
        m = min(2, n - 1)
        G = nx.barabasi_albert_graph(n, m, seed=nx_seed)
    else:
        # Larger network: dual attachment keeps heterogeneity while reducing
        # chain-like structures from degree-sequence pairing.
        m1 = 1
        m2 = min(5, n - 1)
        p = 0.8
        G = nx.dual_barabasi_albert_graph(n, m1, m2, p, seed=nx_seed)
        G = _add_triadic_closure(G, rng, triad_prob=0.15)

    G = _ensure_connected(G, rng)

    # Relabel nodes to clean 0..n-1
    G = nx.convert_node_labels_to_integers(G)

    return G


def network_summary(G: nx.Graph) -> dict:
    """Return a summary dict of the network's properties."""
    degrees = [d for _, d in G.degree()]
    return {
        "n_nodes": G.number_of_nodes(),
        "n_edges": G.number_of_edges(),
        "mean_degree": np.mean(degrees),
        "median_degree": float(np.median(degrees)),
        "min_degree": min(degrees),
        "max_degree": max(degrees),
        "density": nx.density(G),
    }


if __name__ == "__main__":
    # Quick sanity check
    for n in [5, 10, 20, 40, 80, 160, 320]:
        G = generate_network(n, seed=42)
        s = network_summary(G)
        print(f"n={n:>4d} | edges={s['n_edges']:>5d} | "
              f"deg mean={s['mean_degree']:.1f} med={s['median_degree']:.0f} "
              f"min={s['min_degree']} max={s['max_degree']} | "
              f"connected={nx.is_connected(G)}")
