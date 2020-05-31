# coding: utf-8

from typing import List


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children  # 列表类型


class Solution(object):
    """N叉树前序遍历"""
    def preorder(self, root: Node) -> List[int]:
        """递归实现"""
        if not root: return []
        res = []

        def helper(root):
            if root:
                print('root: {}'.format(root.val))
                res.append(root.val)
                for child in root.children:  # 遍历每个子结点
                    print('child: {}'.format(child.val))
                    helper(child)
            print('res: {}'.format(res))
        
        helper(root)
        return res

    def preorder_1(self, root: Node) -> List[int]:
        """迭代实现"""
        if not root: return []
        res = [root]
        stack = []

        while stack:  # 树遍历迭代，判断条件都是这个
            print('stack: {}'.format([s.val for s in stack]))
            node = stack.pop()
            res.append(node.val)
            
            stack.extend(node.children[::-1])  # 逆序压入栈中
            # if node.children:
            #     for child in node.children[::-1]:
            #         stack.append(child)
        
        return res
