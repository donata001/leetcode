# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        if not root: return 0
        return self.helper(root, sum) + self.pathSum(root.left, sum)+self.pathSum(root.right, sum)
        # 这里两种迭代，对于计算每个node要重新计算的情况

    def helper(self, node, acc):
        if not node:
            return 0
        acc-=node.val
        return int(acc==0) +self.helper(node.left, acc)+self.helper(node.right, acc)

