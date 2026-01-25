from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image

        rows, cols = len(image), len(image[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        original = image[sr][sc]
        q = deque([(sr, sc)])
        image[sr][sc] = color
        
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original):
                    q.append((nr, nc))
                    image[nr][nc] = color
            

        return image