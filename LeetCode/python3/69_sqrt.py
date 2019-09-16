class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left,right = 1,x
        while right-left>1:
            mid = (left + right) // 2
            midsquare = mid**2
            if midsquare < x:
                left = mid
            elif midsquare > x:
                right = mid
            else:
                return mid
        return left