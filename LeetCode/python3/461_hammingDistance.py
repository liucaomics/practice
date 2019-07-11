class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''
        dist = 0
        while x or y:
            if x % 2 != y % 2:
                dist +=1
            x = x // 2
            y = y // 2
        return dist
        '''
        xor = x ^ y
        dist = 0
        while xor:
            dist += xor & 1
            xor = xor >> 1
        return dist