class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return 0
        if N==1:
            return 1
        F = [0]*(N+1)
        F[0], F[1] = 0,1
        for i in range(2,N+1):
            F[i] = F[i-1] + F[i-2]
        return F[N]
            
        