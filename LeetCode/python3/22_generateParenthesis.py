class Solution:
    out = []
    def generateParenthesis(self, n: int) -> List[str]:
        self.out = []
        self.generateParenthesis_util('',0,0,n)
        return self.out
    def generateParenthesis_util(self,path,left,right,n):
        if left==n and right==n:
            self.out.append(path)
            return
        if left+1<=n:
            self.generateParenthesis_util(path+'(',left+1,right,n)
        if right+1<=left:
            self.generateParenthesis_util(path+')',left,right+1,n)
