from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    q.append((row, col))
                else:
                    mat[row][col] = float('inf')

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and mat[r][c] + 1 < mat[nr][nc]:
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))

        return mat

        

