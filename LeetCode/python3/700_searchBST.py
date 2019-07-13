# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        p = root
        stack = [p]
        while stack:
            p = stack.pop()
            if p.val == val:
                return p
            elif p.val < val:
                 if p.right:
                        stack.append(p.right)
            elif p.left:
                stack.append(p.left)
        return None
                