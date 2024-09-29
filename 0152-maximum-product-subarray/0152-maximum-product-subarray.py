class Solution:
    def maxProduct(self, nums: List[int]) -> int:
            res = nums[0]  # Initialize result to the first element
            current_max = nums[0]  # Current maximum product
            current_min = nums[0]  # Current minimum product (to handle negative numbers)

            for i in range(1, len(nums)):
                if nums[i] < 0:
                    current_max, current_min = current_min, current_max  # Swap when encountering a negative number
                
                current_max = max(nums[i], current_max * nums[i])
                current_min = min(nums[i], current_min * nums[i])

                res = max(res, current_max)

            return res