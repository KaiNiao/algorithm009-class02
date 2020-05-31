# coding: utf-8

from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """树的前序遍历"""
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        """递归实现"""
        res = []  # 内部函数的外部变量，用于保存遍历的序列

        def helper(root):
            if root:
                res.append(root.val)
                helper(root.left)
                helper(root.right)

        helper(root)        
        return res

    def preorder_traversal_1(self, root: TreeNode) -> List[int]:
        """迭代实现"""
        res = []
        stack = []

        if root: stack.append(root)  # 初始时栈非空
        while stack:  # 将每个结点作为根结点进行处理，即遍历每根子树
            node = stack.pop()
            res.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return res
