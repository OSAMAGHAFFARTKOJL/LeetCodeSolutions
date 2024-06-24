# class Solution:
#   def minKBitFlips(self, nums: List[int], k: int) -> int:
#     res = 0
#     for i in range(0,(len(nums)-k)+1):
#         temp = nums[i:i+k]
#         if 0 in temp and nums[i] == 0:
#             for j in range(i,i+k):
#                 if nums[j] == 0:
#                     nums[j] = 1
#                 elif nums[j] == 1:
#                     nums[j] = 0
#             res +=1
#             i+=k

#     if 0 in nums:
#         return -1
#     else:
#         return res
#Logic work but not efficient and time limit exceed

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        flip = 0  # To keep track of the flip state at each position
        is_flipped = [0] * n  # To record if we have flipped at this position

        for i in range(n):
            if i >= k:
                flip ^= is_flipped[i - k]  # Unflip the k distance away bit if we are past k length

            if nums[i] == flip:  # If the current bit is 0 after flips (flip is 0) or 1 after flips (flip is 1)
                if i + k > n:  # Not enough space to flip k bits
                    return -1
                res += 1  # Count this flip
                flip ^= 1  # Toggle the flip state
                if i + k < n:
                    is_flipped[i] = 1  # Mark the position where the flip starts

        return res


   
