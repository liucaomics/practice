class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            T = [0,1,1] + [0]*(n-2)
            for i in range(n-2):
                T[i+3] = T[i+2] + T[i+1] + T[i]
            return T[-1]