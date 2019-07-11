class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        out = [a**2 for a in A]
        out.sort()
        return out