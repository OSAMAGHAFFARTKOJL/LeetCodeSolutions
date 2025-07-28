# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev_node = TreeNode(float('-inf'))
        
        def dfs(node):
            if not node:
                return 
     
            dfs(node.left)
            if node.val<self.prev_node.val:
                if not self.first:
                    self.first = self.prev_node
                self.second = node
            
            self.prev_node = node

            prev_root = node
            dfs(node.right)
        dfs(root)
        if self.first and self.second:
            self.first.val,self.second.val = self.second.val,self.first.val