class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        list_out = []
        for row in A:
            list_out.append( [ 1-i for i in row[::-1]] )
        return list_out

