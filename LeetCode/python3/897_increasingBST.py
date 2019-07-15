# Definition for a binary tree node.
#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    output = None
    rightMostNode = None
    def rightMostNode(self,node):
        while node.right:
            node = node.right
        return node

    def inOrderTraverse(self, node):
        if node is None:
            return
        # left
        if node.left:
            self.inOrderTraverse(node.left)
        # mid
        if self.output is None:
            self.output = TreeNode(node.val)
            self.rightMostNode = self.output
        else:
            self.rightMostNode.right = TreeNode(node.val)
            self.rightMostNode = self.rightMostNode.right
        # right
        if node.right:
            self.inOrderTraverse(node.right)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.output = None
        rightMostNode = None
        self.inOrderTraverse(root)
        return self.output
        