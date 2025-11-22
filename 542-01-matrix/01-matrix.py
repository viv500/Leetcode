from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        # find all 0s
        # need a visited set cuz non 0 cells could be visited, no other way to check
        # NOTE: cant create set of lists (sets are immutable) add tuples instead
        # time: O(n^2)
        # space O(n^2)

        visited = set()

        rows, cols = len(mat), len(mat[0])

        q = deque()

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    q.append([row, col])
                    visited.add((row, col))


        # multi source bfs
        while q:
            level_size = len(q)

            for _ in range(level_size):
                r, c = q.popleft()

                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        mat[nr][nc] = mat[r][c] + 1 # shortest path
                        q.append([nr, nc])
                        visited.add((nr, nc))
        return mat

