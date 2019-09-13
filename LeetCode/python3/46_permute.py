'''
class Solution:
    out = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.out = []
        self.permute_util([],nums)
        return self.out
    def permute_util(self, current, state):
        if len(state) == 0:
            self.out.append(current)
            return
        for index, s in enumerate(state):
            self.permute_util(current+[s],state[:index] + state[index+1:])
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums, len(nums))
            
    
        
        