class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        start = 0
        end = 0
        S_out = ""
        for i in range(len(S)):
            if stack:
                if stack[-1] == '(' and S[i] == ')':
                    stack.pop()
                    if not stack:
                        end=i
                        primitive = S[start:end+1]
                        S_out += primitive[1:-1]
                        start = end + 1
                else:
                    stack.append(S[i])
            else:
                stack.append(S[i])
        return S_out
                
            
            