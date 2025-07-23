# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        depth = 0
        while q:
            for i in range(len(q)):
                data = q.popleft()
                if data.left:
                    q.append(data.left)
                if data.right:
                    q.append(data.right)
            depth += 1
        return depth