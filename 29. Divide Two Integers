class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        x = int(dividend / divisor)
        if x > 2**31 - 1:
            return 2**31 - 1
        elif x < -2**31:
            return -2**31
        else:
            return x
