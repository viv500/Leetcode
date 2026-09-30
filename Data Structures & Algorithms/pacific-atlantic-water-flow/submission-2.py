from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        p_set, a_set = set(), set()
        p_que, a_que = deque(), deque()

        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    p_set.add((row, col))
                    p_que.append((row, col))
                if row == rows - 1 or col == cols - 1:
                    a_set.add((row, col))
                    a_que.append((row, col))


        while p_que:
            r, c = p_que.popleft()

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in p_set:
                    p_que.append((nr, nc))
                    p_set.add((nr, nc))

        while a_que:
            r, c = a_que.popleft()

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in a_set:
                    a_que.append((nr, nc))
                    a_set.add((nr, nc))


        return [[x,y] for x,y in (a_set & p_set)]

        