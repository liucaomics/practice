'''
class Solution:
    out = []
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def letterCasePermutation(self, S: str) -> List[str]:
        self.out = []
        self.letterCasePermutation_util(S,"",0)
        return self.out
    
    def letterCasePermutation_util(self,S,state,length):
        if length == len(S):
            self.out.append(state)
            return
        if S[length] in self.alphabet:
            self.letterCasePermutation_util(S,state+S[length].upper(),length+1)
            self.letterCasePermutation_util(S,state+S[length].lower(),length+1)
        else:
            self.letterCasePermutation_util(S,state+S[length],length+1)
'''        

# divide and conquer
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if len(S) <= 1:
            if S.upper() == S.lower():
                return [S]
            elif S.upper() == S:
                return [S,S.lower()]
            else:
                return [S,S.upper()]
        mid = int(len(S) / 2)
        left = self.letterCasePermutation(S[:mid])
        right = self.letterCasePermutation(S[mid:])
        return [x+y for x in left for y in right]
        