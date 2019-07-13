# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def length(l):
    out = 0
    p = l
    while p:
        out += 1
        p = p.next
    return out

def add(l,val):
    flag = 0
    p = l
    p.val = p.val + val
    flag = p.val // 10
    p.val = p.val % 10
    while flag != 0:
        if p.next:
            p = p.next
            p.val += flag
            flag = p.val // 10
            p.val = p.val % 10
        else:
            p.next = ListNode(flag)
            break

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        len1, len2 = length(l1), length(l2)
        p1, p2 = l1, l2
        if len1 >= len2:
            for i in range(len2):
                add(p1,p2.val)
                p1 = p1.next
                p2 = p2.next
            return l1
        else:
            for i in range(len1):
                add(p2,p1.val)
                p1 = p1.next
                p2 = p2.next
            return l2
                
                
        
                
        