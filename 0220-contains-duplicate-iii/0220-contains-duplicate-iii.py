class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        for i in range(len(nums)-1):
            j=i+1
            while abs(i-j)<=indexDiff and j < len(nums): 
                if abs(nums[i]-nums[j]) <= valueDiff:
                    return True
                j+=1
        return False

        