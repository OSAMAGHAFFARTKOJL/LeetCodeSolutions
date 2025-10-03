class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # pointers
        l = 0
        h = len(nums)-1
        m = 0
        while m <=h:
            # conditions
            if nums[m] == 0:
                nums[m],nums[l] = nums[l],nums[m]
                l +=1 # low pointer update
                m +=1
            elif nums[m] == 1:
                m +=1  
            else:
                nums[m],nums[h] = nums[h],nums[m]
                h -= 1
          
 
        