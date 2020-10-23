class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree1(self, p: TreeNode, q: TreeNode) -> bool:
        i = []
        j = []
        stack1 = [p]
        while len(stack1) > 0:
            i.append(p.val)
            if p.right:
                stack1.append(p.right)
            if p.left:
                stack1.append(p.left)
            p = stack1.pop()

        stack1 = [q]
        while len(stack1) > 0:
            j.append(q.val)
            if q.right:
                stack1.append(q.right)
            if q.left:
                stack1.append(q.left)
            q = stack1.pop()
        if i == j:
            return True
        else:
            return False

"""
Author:  Mr.Han
Create:  2020/10/23 11:46
Github:  https://github.com/langlang0
Copyright (c) 2020, Mr.Han Group All Rights Reserved.
"""

