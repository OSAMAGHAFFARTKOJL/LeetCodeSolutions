
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize res with a very small number
        res = [float('-inf')]

        def dfs(node):
            if not node:
                return 0
            # Compute max sum on left and right subtrees, only consider positive sums
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            # Update global maximum: node value + max possible sums from both subtrees
            res[0] = max(res[0], node.val + left_max + right_max)
            # Return max path sum where 'node' is the highest parent to use
            return node.val + max(left_max, right_max)

        dfs(root)
        return res[0]
