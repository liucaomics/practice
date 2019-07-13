"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    depth = 0
    
    def traverse(self, curNode, curDepth):
        if curNode:
            curDepth += 1
            if curDepth > self.depth:
                self.depth = curDepth
            for child in curNode.children:
                self.traverse(child,curDepth)
    def maxDepth(self, root: 'Node') -> int:
        self.depth = 0
        self.traverse(root,0)
        return self.depth
        