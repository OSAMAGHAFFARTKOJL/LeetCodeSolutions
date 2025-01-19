class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output













        # ans=[]
        # heap = []
        # for i in range((len(nums)-k)+1):
        #     res = nums[i:i+k]
        #     i=0
        #     while i<k:
        #         heapq.heappush(heap, -1*res[i])
        #         i+=1
        #     ans.append(-1*heapq.heappop(heap))
        #     while heap:
        #         heapq.heappop(heap)
        # return ans