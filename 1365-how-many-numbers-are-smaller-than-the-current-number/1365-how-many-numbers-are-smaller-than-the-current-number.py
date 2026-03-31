class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = {}
        for i in nums:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 1
        res = []
        for i in nums:
            num_iter = i-1
            num = 0
            while num_iter>=0:
                if num_iter in cnt:
                    num += cnt[num_iter]
                num_iter -= 1
            res.append(num)
        return res
