class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            out = int('-'+s[1:][::-1])
            if out < -2**31:
                return 0
            else:
                return out
        else:
            out = int(s[::-1])
            if out > 2**31 -1:
                return 0
            else:
                return out
        