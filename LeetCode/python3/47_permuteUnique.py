
class Solution:
    out = []
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.out = []
        nums.sort()
        self.permuteUnique_util([],nums)
        return self.out
    def permuteUnique_util(self,path,state):
        if len(state) == 0:
            self.out.append(path)
            return
        self.permuteUnique_util(path+[state[0]],state[1:])
        for i in range(1,len(state)):
            if state[i] == state[i-1]:
                continue
            self.permuteUnique_util(path+[state[i]],state[:i]+state[i+1:])
'''        
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, path):
            if not nums:
                ans.append(path)
                return
            i = 0
            while i < len(nums):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]])
                while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    i += 1
                i += 1

        ans = []
        nums.sort()
        dfs(nums, [])
        return ans
'''