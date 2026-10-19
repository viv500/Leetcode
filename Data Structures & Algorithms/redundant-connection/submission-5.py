class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        rank = [0] * (len(edges) + 1)

        def find(a):
            while a != parent[a]:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        def union(a, b):
            parent_a, parent_b = find(a), find(b)
            if parent_a == parent_b: return False

            if rank[b] > rank[a]:
                b, a = a, b

            if rank[a] == rank[b]:
                rank[a] += 1
            
            parent[parent_b] = parent_a
            return True

        for u, v in edges:
            if not union(u, v): return [u, v]