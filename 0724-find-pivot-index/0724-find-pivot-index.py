class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums.insert(0,0)
        nums.insert(len(nums),0)
        for i in range(1,len(nums)-1):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i-1
        return -1

        