class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Approach: Union-Find.
        #
        # Two nodes share a root iff they're already connected. So when we
        # try to union an edge (u, v) and find(u) == find(v), that edge is
        # the one closing a cycle -- exactly the redundant edge.
        #
        # A tree on n nodes has n - 1 edges. The input has n edges (one
        # extra), so exactly one edge creates a cycle. Processing edges in
        # order, the first such edge is the answer: the problem guarantees
        # the redundant edge is the last one in the input that completes a
        # cycle, and any earlier "cycle-closing" edge would contradict the
        # input being a tree plus one extra.

        n = len(edges)
        parent = list(range(n + 1))  # 1-indexed; each node starts as its own root
        rank = [1] * (n + 1)         # size of the component; only roots hold meaningful values

        def find(x):
            # Path compression: point every node on the lookup path directly
            # at the root. Combined with union-by-size, this gives effectively
            # O(alpha(n)) per operation -- alpha is the inverse Ackermann,
            # ~constant for any realistic input.
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            ru, rv = find(u), find(v)
            if ru == rv:
                return False  # already connected -- this edge would create a cycle

            # Union by size: attach the smaller tree under the larger root
            # to keep trees shallow. Rank only ever grows since components
            # only merge, never split.
            if rank[rv] > rank[ru]:
                ru, rv = rv, ru  # ensure ru is the larger root
            parent[rv] = ru
            rank[ru] += rank[rv]
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]