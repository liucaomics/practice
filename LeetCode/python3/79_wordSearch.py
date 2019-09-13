class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False]*len(board[0]) for i in range(len(board))]
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    visited[x][y] = True
                    if self.exist_util(board,word,[x,y],1,visited):
                        return True
                    visited[x][y] = False
        return False
    
    def exist_util(self,board,word,path,num,visited):
        if num == len(word):
            return True
        for x,y in self.children(board,path[0],path[1],word[num]):
            if not visited[x][y]:
                visited[x][y] = True
                if self.exist_util(board,word,[x,y],num+1,visited):
                    return True
                visited[x][y] = False
        return False
    
    def children(self,board,x,y,char):
        out = []
        if y-1>=0 and board[x][y-1] == char:
            out.append([x,y-1])
        if y+1<len(board[0]) and board[x][y+1] == char:
            out.append([x,y+1])
        if x-1>=0 and board[x-1][y] == char:
            out.append([x-1,y])
        if x+1<len(board) and board[x+1][y] == char:
            out.append([x+1,y])
        return out
        