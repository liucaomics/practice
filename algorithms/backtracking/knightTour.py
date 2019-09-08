'''
https://en.wikipedia.org/wiki/Knight%27s_tour
Find one path of knight tour (no repitition) which covers all the positions of the board (8x8)
'''

def is_valid(x,y,board):
    if x < 0 or y < 0 or x > 7 or y > 7:
        return False
    elif board[x][y] > 0:
        return False
    else:
        return True

def solveKT():
    n = 8
    board = [[-1]*n for i in range(n)]
    board[0][0] = 0
    pos = 1
    move_x = [2,2,-2,-2,1,1,-1,-1]
    move_y = [1,-1,-1,-1,2,-2,2,-2]
    if(not solveKTUtil(board, 0, 0, move_x, move_y, pos)): 
        print("Solution does not exist") 
    else: 
        for i in board:
            print(i)

def solveKTUtil(board,x,y,move_x, move_y, pos):
    print(pos)
    if pos == 8**2:
        return True
    for i in range(8):
        new_x = x + move_x[i]
        new_y = y + move_y[i]
        if is_valid(new_x,new_y,board):
            board[new_x][new_y] = pos
            if solveKTUtil(board,new_x,new_y,move_x,move_y,pos+1):
                return True
            # backtracking
            board[new_x][new_y] = -1
    return False


if __name__ == '__main__':
    solveKT()




