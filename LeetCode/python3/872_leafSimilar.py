# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        seq1 = []
        seq2 = []
        self.preOrderSearch(root1,seq1)
        self.preOrderSearch(root2,seq2)
        if len(seq1) == len(seq2):
            for i in range(len(seq1)):
                if seq1[i]!=seq2[i]:
                    return False
            return True
        else:
            return False

    def preOrderSearch(self,node,seq):
        if node:
            if not( node.left or node.right):
                seq.append(node.val)
            self.preOrderSearch(node.left,seq)
            self.preOrderSearch(node.right,seq)
        
