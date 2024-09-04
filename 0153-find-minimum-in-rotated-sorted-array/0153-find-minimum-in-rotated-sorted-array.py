class Solution:
    def findMin(self, nums: List[int]) -> int:

        return min(nums)
#Another approach
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         length=len(nums)
#         left=0
#         right=length-1
#         while left<right:
#             mid=(left+right)//2
#             if nums[mid]>nums[right]:
#                 left=mid+1
#             else:
#                 right=mid
#         return nums[left]

        