class MedianFinder:

    def __init__(self):
        # It initialze heap in global scope
        self.small , self.large = [],[]
        

    def addNum(self, num: int) -> None:
        # Put the nums in the heap
        if self.large and num > self.large[0] :
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-1 * num)

        # Make the size of each heap adjusted
        if len(self.large) > len(self.small) + 1 :
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        if len(self.small) > len(self.large) + 1 :
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large ,  val)

        
        

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.large) < len(self.small):
            return -1 * self.small[0]
        else:
            return ((-1 * self.small[0])+ self.large[0])/2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
