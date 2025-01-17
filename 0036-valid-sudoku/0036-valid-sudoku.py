class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        for i in range(row):
            x = set()
            for j in range(col):
                if board[i][j].isdigit() and board[i][j] not in x:  
                    x.add(board[i][j])
                elif board[i][j] in x:
                    return False
                
        for i in range(row):
            x = set()
            for j in range(col):
                if board[j][i].isdigit() and board[j][i] not in x:
                    x.add(board[j][i])
                elif board[j][i] in x:
                    return False
        count = 0
        box1 = set()
        box2 = set()
        box3 = set()
        for i in range(row):
            for j in range(col):
                if j>=0 and j<=2:
                    if board[i][j].isdigit() and board[i][j] not in box1:  
                        box1.add(board[i][j])
                    elif board[i][j] in box1:
                        return False
                elif j>=3 and j<=5:
                    if board[i][j].isdigit() and board[i][j] not in box2:  
                        box2.add(board[i][j])
                    elif board[i][j] in box2:
                        return False
                elif j>=6 and j<=8:
                    if board[i][j].isdigit() and board[i][j] not in box3:  
                        box3.add(board[i][j])
                    elif board[i][j] in box3:
                        return False
            count+=1
            if count == 3:
                count = 0
                box1.clear()
                box2.clear()
                box3.clear()

        return True

                
