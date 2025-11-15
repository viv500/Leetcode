class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # 0 is islands 1 is water
        # flood all borders (set borders to 1) , run regular algoirthm

        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        closed_islands = 0

        visited = set() # if space is a concern, modify input array with 1s
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] == 1:
                return

            visited.add((r, c))

            dfs(r, c - 1)
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c + 1)

        # bad border flooding: this only marks border as visited -> this will lead to non closed islands being assumed as closed
        # for i in range(rows):
            # for j in range(cols):
                # if i == 0 or j == 0:
                    # visited.add((i, j))

        # need to mark an ENTIRE border touching island visited but not increment island count
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r == 0 or c == 0 or r == rows - 1 or c == cols - 1):
                    dfs(r, c)



        # regular number of islands
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and (i, j) not in visited:
                    closed_islands += 1
                    dfs(i, j)

        return closed_islands



        