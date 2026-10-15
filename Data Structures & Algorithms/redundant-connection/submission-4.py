class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        def union(a, b):
            parent[find(a)] = find(b)

        def find(a):
            while a != parent[a]:
                parent[a] = parent[parent[a]]
                a = parent[a]         
            return a


        for u, v in edges:
            if find(u) == find(v): return [u, v]

            union(u, v)

