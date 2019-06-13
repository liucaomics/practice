class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total = 0
        for i in S:
            if i in J:
                total += 1
        return total