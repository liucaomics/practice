class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        # first check adjacent element
        # if no repeated elements, check first 4 elements
        '''
        N = len(A)
        for i in range(N-1):
            if A[i] == A[i+1]:
                return A[i]
        if A[0] == A[2]:
            return A[0]
        elif A[0] == A[3]:
            return A[0]
        else:
            return A[1]
        '''
        
        '''
        N = len(A)
        for i in range(N-1):
            for j in range(i+1,N):
                if A[i] == A[j]:
                    return A[i]
        '''
        hashCount = dict()
        for a in A:
            hashCount[a] = hashCount.get(a,0) + 1
            if hashCount[a] > 1:
                return a
            
            
        