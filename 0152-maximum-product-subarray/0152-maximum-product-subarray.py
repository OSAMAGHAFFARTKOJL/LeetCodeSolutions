class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        l=0
        while l<len(nums) :
            for i in range(l+1,len(nums)+1):
                x = prod(nums[l:i])
                if x >res:
                    res = x
            l+=1
        return res