from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, current_sum, path):
            if not node:
                return

            # Add current node to the path and update sum
            path.append(node.val)
            current_sum += node.val

            # If it's a leaf node and the sum matches target
            if not node.left and not node.right:
                if current_sum == targetSum:
                    res.append(path[:])  # copy the current path

            # Recurse left and right
            dfs(node.left, current_sum, path)
            dfs(node.right, current_sum, path)

            # Backtrack
            path.pop()

        dfs(root, 0, [])
        return res
