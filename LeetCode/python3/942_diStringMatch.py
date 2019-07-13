class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        '''
        num_D = 0
        for i in S:
            if i == 'D':
                num_D += 1
        out = [num_D]
        pD = num_D - 1
        pI = num_D + 1
        for i in range(len(S)):
            if S[i] == 'D':
                out.append(pD)
                pD -= 1
            else:
                out.append(pI)
                pI += 1
        return out
        '''
        low, high = 0,len(S)
        out = []
        for i in S:
            if i == 'D':
                out.append(high)
                high -= 1
            else:
                out.append(low)
                low += 1
        return out + [low]
                    
        