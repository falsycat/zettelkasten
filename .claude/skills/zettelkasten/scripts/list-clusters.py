#!/usr/bin/env python3
"""
Compute connected clusters from the zettelkasten note graph.

Usage (from repo root):
    python3 .claude/skills/zettelkasten/scripts/list-clusters.py

Output (TSV, sorted by cluster size desc, then node ID):
    <cluster_num>\t<node_id>\t<title>
"""

import subprocess
import sys
from collections import defaultdict
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
REPO_ROOT = SKILL_DIR.parent.parent


def _run(script):
    result = subprocess.run(
        ["bash", str(script)], capture_output=True, text=True, cwd=REPO_ROOT
    )
    return result.stdout.strip()


def get_edges():
    out = _run(SKILL_DIR / "scripts" / "list-deps.sh")
    edges = []
    for line in out.split("\n"):
        if "\t" in line:
            s, t = line.split("\t", 1)
            edges.append((s.strip(), t.strip()))
    return edges


def get_titles():
    out = _run(SKILL_DIR / "scripts" / "list-titles.sh")
    titles = {}
    for line in out.split("\n"):
        if "\t" in line:
            file_id, title = line.split("\t", 1)
            node_id = file_id.split("-")[0]
            titles[node_id] = title.strip()
    return titles


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[rb] = ra


def compute_clusters(edges, all_nodes):
    uf = UnionFind()
    for s, t in edges:
        uf.union(s, t)
    for n in all_nodes:
        uf.find(n)

    groups = defaultdict(list)
    for n in all_nodes:
        groups[uf.find(n)].append(n)
    return sorted(groups.values(), key=lambda g: (-len(g), min(g)))


def main():
    edges = get_edges()
    titles = get_titles()

    all_nodes = set(titles.keys())
    for s, t in edges:
        all_nodes.add(s)
        all_nodes.add(t)

    clusters = compute_clusters(edges, all_nodes)

    for i, members in enumerate(clusters, 1):
        for node in sorted(members):
            title = titles.get(node, "(no title)")
            print(f"{i}\t{node}\t{title}")


if __name__ == "__main__":
    main()
