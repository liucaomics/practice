class Solution:
    def coord(self,board):
        for i in range(len(board[0])):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    return (i,j)
    
    def can_capture(self,L):
        for i in L:
            if i == 'p':
                return True
            elif i == 'B':
                return False
        return False

    def numRookCaptures(self, board: List[List[str]]) -> int:
        N = len(board[0])
        x,y = self.coord(board)
        north = [board[i][y] for i in range(x)][::-1]
        south = [board[i][y] for i in range(x+1,N)]
        east = board[x][y+1:]
        west = board[x][:y][::-1]
        #print(east)
        #print(self.can_capture(east))
        return self.can_capture(north) + self.can_capture(south) + self.can_capture(east) + self.can_capture(west)
        
        
        