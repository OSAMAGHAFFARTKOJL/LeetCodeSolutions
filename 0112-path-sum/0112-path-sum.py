# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.res = False
        def dfs(root,current_sum,target):
            if not root.left and not root.right:
                print(current_sum)
                if current_sum == target:
                    self.res = True
                return 0
            if root.left:
                dfs(root.left,(current_sum + root.left.val),target)
            if root.right:
                dfs(root.right,(current_sum + root.right.val),target)
        dfs(root,root.val,targetSum)   
        return self.res
                
            
        
        