# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        stack1 = [t1]
        stack2 = [t2]
        while stack1:
            #print("####")
            #print(stack1)
            #print(stack2)
            st1 = stack1.pop()
            st2 = stack2.pop()
            st1.val += st2.val
            if st1.left:
                if st2.left:
                    stack1.append(st1.left)
                    stack2.append(st2.left)
            else:
                if st2.left:
                    st1.left = st2.left
            if st1.right:
                if st2.right:
                    stack1.append(st1.right)
                    stack2.append(st2.right)
            else:
                if st2.right:
                    st1.right = st2.right
        return t1
                    
            
            
        