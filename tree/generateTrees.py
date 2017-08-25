# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # 4：26

        def helper(start, end):
            lst = []
            for root in xrange(start, end+1):
                for left in helper(start, root-1):  # 可以输出[None]
                    for right in helper(root+1, end):  #可以输出[None]
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        lst.append(node)
            return lst or [None]
        if not n: return []
        return helper(1, n)

        