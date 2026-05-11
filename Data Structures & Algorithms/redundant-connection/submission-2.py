class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union find works naturally here
        # in union find, being in the same component (i.e. having the same parent) means there was already a connection
        # so if we try unioning 2 nodes and they had the same parent, that edge was the one that introduced the cycle

        # since nodes are numbered from 1 to n

        n = len(edges) # a tree has exactly (n - 1) edges. since the extra edge JUST introduced a cycle, graph has n edges
        parent = [i for i in range(n + 1)] # every node is a parent of itself at the start
        rank = [1] * (n + 1) # number of elements in a particular component

        def find(n):
            if n != parent[n]: # keep going up the tree until the parent is itself
                n = find(parent[n])
            return n

        def union(u1, u2):
            p1, p2 = find(u1), find(u2)

            if p1 == p2: return False # same parent -> there was a connection between them before

            # larger rank root is retained; compare roots not nodes
            if rank[p2] > rank[p1]:
                parent[p1] = p2 # root (parent) of u1 is now rooted under u2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]

            return True


        for u,v in edges:
            if not union(u,v): return [u,v] # the first edge to introduce the cycle is the "edge that appears last in the input edges"


                
            