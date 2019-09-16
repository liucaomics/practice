import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 1:
            return n
        low, high = 0, int(math.sqrt(2*n))+1
        while low+1<high:
            mid = (low + high) // 2
            stair_sum = mid*(mid+1) / 2
            if stair_sum==n:
                return mid
            elif stair_sum<n:
                low = mid
            else:
                high = mid
        return low