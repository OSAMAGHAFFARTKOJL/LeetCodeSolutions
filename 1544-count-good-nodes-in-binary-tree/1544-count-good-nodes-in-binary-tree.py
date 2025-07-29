# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 1
        def dfs(root,val):
            if not root:
                return 
            if root.val>=val:
                self.good_nodes += 1
            
            dfs(root.left,max(root.val,val))
            dfs(root.right,max(root.val,val))
          
        dfs(root.left,root.val)  
        dfs(root.right,root.val)
        return self.good_nodes 
      

        