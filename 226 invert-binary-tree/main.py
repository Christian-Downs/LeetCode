# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return
        if root.right is None and root.left is None:
            return root
        temp = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        root.left = temp
        return root


