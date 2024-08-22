class NumArray:

    def __init__(self, nums: List[int]):
        self.x = nums
        

    def sumRange(self, l: int, r: int) -> int:
        return sum(self.x[l:r+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)