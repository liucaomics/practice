class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        out = []
        for num in range(left, right+1):
            digits = []
            num_old = num
            while num != 0:
                digits.append( num % 10 )
                num = num // 10
            if 0 in digits:
                continue
            else:
                count = 0
                for d in digits:
                    if num_old % d != 0:
                        break
                    else:
                        count += 1
                if count == len(digits):
                    out.append(num_old)
        return out
        