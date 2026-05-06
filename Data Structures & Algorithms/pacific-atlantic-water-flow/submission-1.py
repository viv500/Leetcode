from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # all cells touching the pacfific or atlantic by default, already flow into those oceans
        p_set = set()
        a_set = set()

        p_que = deque()
        a_que = deque()

        rows, cols = len(heights), len(heights[0])

        # bordering rows
        for i in range(cols):
            p_set.add((0, i))
            p_que.append((0, i))

            a_set.add((rows - 1, i))
            a_que.append((rows - 1, i))


        # bordering cols
        for i in range(rows):
            p_set.add((i, 0))
            p_que.append((i, 0))

            a_set.add((i, cols - 1))
            a_que.append((i, cols - 1))
        

        print("a_set: ", a_set)
        print("p_set: ", p_set)

        # pacific bfs
        while p_que:
            row, col = p_que.popleft()

            for dr, dc in directions:
                nr, nc = dr + row, dc + col

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in p_set and heights[nr][nc] >= heights[row][col]:
                    p_que.append((nr, nc))
                    p_set.add((nr, nc))

        # atlantic bfs
        while a_que:
            row, col = a_que.popleft()

            for dr, dc in directions:
                nr, nc = dr + row, dc + col

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in a_set and heights[nr][nc] >= heights[row][col]:
                    a_que.append((nr, nc))
                    a_set.add((nr, nc))

        return [[row, col] for row, col in a_set & p_set]