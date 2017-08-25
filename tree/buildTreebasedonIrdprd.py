# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            nidx = inorder.index(preorder.pop(0))
            node = TreeNode(inorder[nidx])
            node.left = self.buildTree(preorder, inorder[0:nidx])
            node.right = self.buildTree(preorder, inorder[nidx+1:])
            return node