class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i in range(len(heights)-1):
            rect = min(heights[i],heights[i+1])
            stack = []
            if res < rect*2:
                res = rect*2
        return max(res,len(heights)*min(heights),max(heights))

        