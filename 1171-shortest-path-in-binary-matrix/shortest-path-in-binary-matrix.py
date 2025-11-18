from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if not grid or not grid[0]: return -1
        if grid == [[0]]: return 1

        rows, cols = len(grid), len(grid[0])

        # edge cases! top left and bottom right are not 0s
        if grid[0][0] != 0 or grid[rows - 1][cols - 1] != 0: return -1

        q = deque([(0, 0)])
        grid[0][0] = 1

        while(q):
            r, c = q.popleft()

            directions = [[-1, 0], [-1, -1], [-1, 1], [1, 0], [1, -1], [1, 1], [0, -1], [0, 1]]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    # did we reach bottom right?
                    if (nr == rows - 1 and nc == cols - 1):
                        return grid[r][c] + 1
                    else:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr, nc))

        return -1