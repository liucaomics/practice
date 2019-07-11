class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights2 = sorted(heights)
        total = 0
        for i in range(len(heights)):
            if heights2[i] != heights[i]:
                total += 1
        return total
        