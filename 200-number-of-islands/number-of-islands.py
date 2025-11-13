class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            if(r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0" or (r,c) in visited): #input validation
                return

            # mark visited
            grid[r][c] == "0"
            visited.add((r,c)) # to avoid double counting

            # call dfs on all paths
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited: # need to avoid double counting
                    islands += 1
                    dfs(r, c)

        return islands