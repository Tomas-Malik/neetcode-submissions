class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        boxes = [[0]*10 for _ in range(9)]
        for i in range(9):
            r = [0]*10
            c = [0]*10
            for j in range(9):
                box_ix = i // 3 * 3 + j // 3

                if board[i][j] != ".":
                    val = int(board[i][j])
                    r[val] += 1
                    boxes[box_ix][val] += 1
                    if r[val] > 1:
                        return False
                    if boxes[box_ix][val] > 1:
                        return False
                if board[j][i] != ".":
                    val = int(board[j][i])
                    c[val] += 1
                    if c[val] > 1:
                        return False
            
            
        return True

