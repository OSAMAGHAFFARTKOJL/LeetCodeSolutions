class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1 
        res = r
        while l <= r:
            sum_of_time = 0
            k = (l+r) // 2
            for i in (piles):
                sum_of_time += math.ceil(i/k)
            if sum_of_time <= h:
                res = min(res,k)
                r = k - 1
            else:
                l = k+1


        return res

        