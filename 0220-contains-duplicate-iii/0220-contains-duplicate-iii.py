# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
#         l = 0
#         r=1
#         while r<len(nums):
#             if abs(l-r)<=indexDiff:
#                 if abs(nums[l]-nums[r]) <= valueDiff:
#                     return True
#             else:
                
#                 l += 1
#                 r=l

#             r+=1
                
#         return False
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False  # Edge case: valueDiff can't be negative, so return False.
        
        buckets = {}  # Dictionary to store elements by their bucket index.
        
        for i, num in enumerate(nums):  # Iterate over the list with both index and value.
            bucketId = num // (valueDiff + 1)  # Calculate the bucket index for the current element.
            
            # Check if there is an element in the same bucket
            if bucketId in buckets and i - buckets[bucketId][0] <= indexDiff:
                return True  # Same bucket, and indices difference <= indexDiff, return True.
            
            # Check if there is an element in the previous bucket (bucketId - 1)
            if (bucketId - 1 in buckets and 
                i - buckets[bucketId - 1][0] <= indexDiff and 
                abs(num - buckets[bucketId - 1][1]) <= valueDiff):
                return True  # Neighboring bucket and satisfies both index and value conditions.
            
            # Check if there is an element in the next bucket (bucketId + 1)
            if (bucketId + 1 in buckets and 
                i - buckets[bucketId + 1][0] <= indexDiff and 
                abs(num - buckets[bucketId + 1][1]) <= valueDiff):
                return True  # Neighboring bucket and satisfies both index and value conditions.
            
            # Add the current element and its index to the dictionary (in its bucket)
            buckets[bucketId] = (i, num)
        
        return False  # If no such pair is found, return False.

