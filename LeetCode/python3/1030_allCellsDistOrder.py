from collections import deque

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        output = []
        visit = [[False]*C for i in range(R)]
        queue = deque([[r0,c0]])
        visit[r0][c0] = True
        while queue:
            r,c = queue.popleft()
            output.append([r,c])
            if r+1<R and (not visit[r+1][c]):
                queue.append([r+1,c])
                visit[r+1][c] = True
            if r-1>=0 and (not visit[r-1][c]):
                queue.append([r-1,c])
                visit[r-1][c] = True
            if c+1<C and (not visit[r][c+1]):
                queue.append([r,c+1])
                visit[r][c+1] = True
            if c-1>=0 and (not visit[r][c-1]):
                queue.append([r,c-1])
                visit[r][c-1] = True
        return output
        
