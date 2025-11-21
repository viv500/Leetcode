from collections import deque
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        sub_islands = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]


        def bfs(r, c):
            q = deque([(r, c)])
            is_sub_island = True

            while q:
                r, c = q.popleft()

                # dont flood fill grid1 since it could contribute to another island in grid1
                # efficient bfs marks as visited when theyre discovered, not when theyre popped (after adding)
                # cuz this could lead to multiple nodes trying to discover this
                # grid2[r][c] = 0

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if(0 <= nr < rows and 0 <= nc < cols and grid2[nr][nc] == 1): # found land on graph 2
                            if grid1[nr][nc] == 1:
                                # graph 1 also has land here, sub island possible
                                # floodfill and add to queue
                                grid2[nr][nc] = 0
                                q.append((nr, nc))
                            else:
                                # graph 1 has water here -> this island in graph 2 is not a subisland
                                # return False: wrong cuz we still need to "consume" whole island i.e. mark spots visited
                                is_sub_island = False

                
            # reached this point -> all land points in graph2 are land points in graph 1

            # return True same reason
            return is_sub_island


        for row in range(rows):
            for col in range(cols):
                # early exit if grid1 doesnt have a 1, but also check dfs
                if grid2[row][col] == 1 and grid1[row][col] == 1 and bfs(row, col):
                    sub_islands += 1

        return sub_islands



        