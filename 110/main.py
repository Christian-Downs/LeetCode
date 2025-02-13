# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left:TreeNode = left
#         self.right:TreeNode = right
class Solution(object):
    def __init__(self):
        self.balanced = True

    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        self.depth(root, True)
        return self.balanced

    def depth(self, node, root=False):
        if node.right is None and node.left is None:
            if root:
                return True
            return 1
        rDepth = 0
        if node.right is not None:
            rDepth = self.depth(node.right)
        lDepth = 0
        if node.left is not None:
            lDepth = self.depth(node.left)

        if abs(lDepth - rDepth) >= 2:
            print(lDepth)
            print(rDepth)
            print(node.val)
            self.balanced = False

        return rDepth + 1 if rDepth > lDepth else lDepth + 1
