def isValid(board,row,col,num):
    for x in range(9):
        if board[row][x]==num:
            return False

    for x in range(9):
        if board[x][col]==num:
            return False

    startRow=row-row%3
    startCol=col-col%3

    for i in range(3):
        for j in range(3):
            if board[startRow+i][startCol+j]==num:
                return False

    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col]==0:
                for num in range(1,10):
                    if isValid(board,row,col,num):
                        board[row][col]=num
                        if solve(board):
                            return True
                        board[row][col]=0
                return False
    return True

def printBoard(board):
    print("Solve Sudoku.")
    for i in range(9):
        for j in range(9):
            print(board[i][j],end=" ")
        print()

def main():
    board=[]
    for i in range(9):
        print("Enter row",i+1)
        row=list(map(int,input().split()))
        board.append(row)

    if solve(board):
        printBoard(board)
    else:
        print("No solution")

if __name__=="__main__":
    main()
