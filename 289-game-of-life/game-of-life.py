class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # mapping
        # old.  new.  state
        # 0.     0.    0
        # 1.     0.    1
        # 0     1.    2
        # 1.     1.    3

        # logic:      if 1, then survives if nei in [2,3] else die
        #             if 0, then survives if nei == 3 else die

        mapping = {0:0, 1:0, 2:1, 3:1}
        
        rows, cols = len(board), len(board[0])
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        def countNeighbors(row, col):
            count = 0
            for dr, dc in directions:
                nr, nc = dr + row, dc + col

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in [1,3]:
                    count += 1

            
            return count


        for row in range(rows):
            for col in range(cols):
                nei = countNeighbors(row, col)
                if board[row][col] == 1:
                    if nei not in [2,3]:
                        board[row][col] = 1
                    else:
                        board[row][col] = 3
                else:
                    # == 0
                    if nei == 3:
                        board[row][col] = 2
                    # else it stays 0


        for row in range(rows):
            for col in range(cols):
                board[row][col] = mapping[board[row][col]]

        

