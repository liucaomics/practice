def is_increasing(L):
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            return False
    return True

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        good = 0
        for col in zip(*A):
            if is_increasing(col):
                good += 1
        return len(A[0]) - good
