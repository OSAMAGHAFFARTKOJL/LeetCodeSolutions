class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hsh = {}
        ans = 0

        for i in nums:
            if i in hsh:
                hsh[i] +=1
            else:
                hsh[i] = 1

        for i in hsh:
            x = hsh[i]
            if i+1 in hsh: 
                y = hsh[i+1]
                if x and y:
                    z=x+y
                    if z >ans:
                        ans = z
        return ans 


