class Solution:
    def twoSum(self, nums, target):
        # Create a dictionary to store the indices of visited numbers
        num_dict = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_dict:
                return [num_dict[diff], i]
            num_dict[num] = i

        return [] 
