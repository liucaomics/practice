class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        list_odd = []
        list_even = []
        for i in A:
            if i % 2 ==0:
                list_even.append(i)
            else:
                list_odd.append(i)
        return list_even + list_odd
                
        