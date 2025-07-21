# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.countNodes(root)
        return self.max_diameter

    def countNodes(self, root):
        if root is None:
            return 0

        # Get height of left and right subtrees
        left_height = self.countNodes(root.left)
        right_height = self.countNodes(root.right)

        # Update the maximum diameter found so far
        self.max_diameter = max(self.max_diameter, left_height + right_height)

        # Return height of current subtree
        return 1 + max(left_height, right_height)
