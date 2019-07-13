class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ancor = A[0]
        for i in range(1,len(A)):
            ancor2 = ancor
            for a in ancor2:
                if a not in A[i]:
                    ancor = ancor.replace(a,'',1)
                else:
                    A[i] = A[i].replace(a,'',1)
        return list(ancor)
                    