"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution:
    post = []
    def traverse(self,root):
        if not root:
            return
        for i in root.children:
            self.traverse(i)
        self.post.append(root.val)

    def postorder(self, root: 'Node') -> List[int]:
        self.post = []
        self.traverse(root)
        return self.post
        
        