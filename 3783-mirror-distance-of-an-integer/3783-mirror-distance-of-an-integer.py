class Solution:
    def mirrorDistance(self, n: int) -> int:
        str_val = str(n)
        int_val = int(str_val[::-1])
        return abs(n-int_val)