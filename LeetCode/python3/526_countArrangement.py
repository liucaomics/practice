class Solution:
    out = 0
    def countArrangement(self, N: int) -> int:
        self.out = 0
        visited = [False]*(N+1)
        self.countArrangement_util(visited, N)
        return self.out
    
    def countArrangement_util(self, visited, num):
        if num == 0:
            self.out += 1
            return
        for i in range(1,len(visited)):
            if not visited[i]:
                if num % i == 0 or i % num == 0:
                    visited[i] = True
                    self.countArrangement_util(visited, num-1)
                    visited[i] = False
 