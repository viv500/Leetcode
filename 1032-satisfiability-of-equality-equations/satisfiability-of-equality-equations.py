class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        parent = list(range(26))

        def union(x, y):
            parent[find(x)] = find(y)

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            
            return x

        def idx(char):
            return ord(char) - ord('a')

        for eq in equations:
            a, op, _, b = eq
            a = idx(a)
            b = idx(b)
            if op == "=":
                union(find(a), find(b))
            
        for eq in equations:
            a, op, _, b = eq
            a = idx(a)
            b = idx(b)
            if op == "!":
                if find(a) == find(b): return False
        
        return True

        

        