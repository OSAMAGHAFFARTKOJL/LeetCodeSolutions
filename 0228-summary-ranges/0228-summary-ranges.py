class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = 0 
        ans = []

        for r in range(len(nums)):
            # Check if the current element is the last one or not consecutive with the next one
            if r == len(nums) - 1 or nums[r] + 1 != nums[r + 1]:
                if l == r:
                    ans.append(f"{nums[r]}")
                else:
                    ans.append(f"{nums[l]}->{nums[r]}")
                l = r + 1


        return ans


        