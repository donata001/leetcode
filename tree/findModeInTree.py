# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter

class Solution(object):
    def __init__(self):
        self.mode = []

    def findMode(self, root):
        if not root: return []
        self.bookIt(root)
        m = Counter(self.mode)
        max_count = max(m.values())
        return [k for k in m if m[k] == max_count ]

    def bookIt(self, node):
        if not node: return
        self.mode.append(node.val)
        self.bookIt(node.left)
        self.bookIt(node.right)
        return

#最原始的方法一定要记得用hashmap数数