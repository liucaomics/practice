class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        v_odd = []
        v_even = []
        out = []
        for a in A:
            if a % 2 == 0:
                v_even.append(a)
            else:
                v_odd.append(a)
        for i in range(len(v_even)):
            out.append(v_even[i])
            out.append(v_odd[i])
            
        return out
            