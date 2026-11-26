class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        output = []
        trie = {}
        path = set()

        for word in words:
            d = trie
            for char in word:
                if char not in d:
                    d[char] = {}
                d = d[char]
            d["!"] = word

        rows, cols = len(board), len(board[0])

        def dfs(node, r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in path or board[r][c] not in node: return

            node = node[board[r][c]]

            if "!" in node: 
                output.append(node["!"])
                del node["!"] # to avoid dupes

            path.add((r, c))
    
            dfs(node, r, c + 1)
            dfs(node, r + 1, c)
            dfs(node, r - 1, c)
            dfs(node, r, c - 1)

            path.remove((r, c))

        
        for row in range(rows):
            for col in range(cols):
                dfs(trie, row, col)
        

        return output