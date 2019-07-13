class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        '''
        for i in range(1,len(A)-1):
            if A[i] > A[i+1]:
                return i
        '''
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if A[mid] > A[mid+1]:
                hi = mid
            else:
                lo = mid+1
        return lo