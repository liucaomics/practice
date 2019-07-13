class Solution:
    def top(self, grid):
        out = 0
        for i in range(len(grid[0])):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    out += 1
        return out
    
    def side(self,grid):
        return sum(map(max,grid))
    
    def front(self,grid):
        out = 0
        for i in zip(*grid):
            out+=max(i)
        return out
                
    def projectionArea(self, grid: List[List[int]]) -> int:
        return self.top(grid) + self.side(grid) + self.front(grid)
        