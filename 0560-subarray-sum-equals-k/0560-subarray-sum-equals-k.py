class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        hash_map = {0:1}
        prefix = 0
        for num in nums:
            prefix += num
            if (prefix - k) in hash_map :
                count += hash_map[prefix-k]
            hash_map[prefix] = hash_map.get(prefix,0) + 1
        return count
        # l = 0
        # r = 1
        # count = 0
        # while l < len(nums):
        #     sums = sum(nums[l:r])
        #     if sums == k:
        #         count += 1
        #     if r == len(nums) :
        #         l += 1
        #         r = l
            
        #     r += 1
        # return count


