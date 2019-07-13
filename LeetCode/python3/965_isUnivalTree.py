# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        #print(root.val)
        #if not root:
        #    return False
        stack = [root]
        value = root.val
        while stack:
            p = stack.pop()
            if p.val != value:
                return False
            if p.left:
                stack.append(p.left)
            if p.right:
                stack.append(p.right)       
        return True

