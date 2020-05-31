# coding: utf-8

from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """中序遍历"""
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        """递归实现"""
        res = []

        def helper(root):
            if root:
                helper(root.left)
                res.append(root.val)
                helper(root.right)
        helper(root)

        return res

    def inorder_traversal_1(self, root: TreeNode) -> List[int]:
        """迭代实现"""
        res = []
        if not root: return res

        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res
