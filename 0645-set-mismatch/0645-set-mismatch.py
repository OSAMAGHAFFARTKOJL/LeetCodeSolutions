class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = 0
        dup_find = set()
        for i in nums:
            if i in dup_find:
                dup = i
            dup_find.add(i)

       
        for i in range(len(nums)):
            if i+1 not in dup_find:
                return [dup,i+1]
        