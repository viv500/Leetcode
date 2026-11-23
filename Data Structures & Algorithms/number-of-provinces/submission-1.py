class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        parent = [i for i in range(n)]
        rank = [0] * n

        def union(a, b):
            x, y = find(a), find(b)
            if x == y: return False

            if rank[x] < rank[y]:
                x, y = y, x

            parent[y] = x

            if rank[x] == rank[y]:
                rank[x] += 1

            return True

        def find(a):
            while a != parent[a]:
                parent[a] = parent[parent[a]]
                a = parent[a]
            
            return a

        
        components = n

        for row in range(n):
            for col in range(n):
                if isConnected[row][col]:
                    if union(row, col): components -= 1

        return components
