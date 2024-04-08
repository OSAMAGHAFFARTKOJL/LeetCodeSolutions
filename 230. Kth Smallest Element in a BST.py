
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         arr = []
        
#         def asp(root):
#             if root is None:
#                 return
#             asp(root.left)
#             arr.append(root.val)
#             asp(root.right)
        
#         asp(root)
#         return arr[k-1]
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root 
        while stack or cur :
            while cur :
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k-=1
            if k == 0 :
                return cur.val
            cur = cur.right
