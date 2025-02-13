# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.traversal = []

    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is not None:
            self.looksie(root)
        return self.traversal

    def looksie(self, node):
        self.traversal.append(node.val)
        if node.left is None and node.right is None:
            return

        if node.left is not None:
            self.looksie(node.left)
        if node.right is not None:
            self.looksie(node.right)
