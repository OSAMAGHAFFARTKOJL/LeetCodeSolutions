class Solution:
    def findLHS(self, nums: List[int]) -> int:

        ans = 0
        for i in nums:
            x = nums.count(i)
            y = nums.count(i+1)
            if x and y:
                z=x+y
                if z >ans:
                    ans = z
        return ans 


