# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#def getsum(node, L, R, total):
#    if node is not None:
#        if node.val >= L and node.val <= R:
#            total[0] += node.val
#        getsum(node.left,L,R,total)
#        getsum(node.right,L,R,total)

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        total = 0
        stack_TreeNode = [root]
        while len(stack_TreeNode) > 0:
            node = stack_TreeNode.pop()
            if node is None:
                continue
            if node.val < L:
                stack_TreeNode.append(node.right)
            elif node.val > R:
                stack_TreeNode.append(node.left)
            else:
                stack_TreeNode.append(node.right)
                stack_TreeNode.append(node.left)
                total += node.val
        return total
#    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
#        total = [0]
#        getsum(root,L,R,total)
#        return total[0]
    
        
        
        