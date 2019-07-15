class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [list(i) for i in zip(*A)]




