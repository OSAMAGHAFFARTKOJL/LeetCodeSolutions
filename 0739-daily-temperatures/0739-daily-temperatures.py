from typing import List

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        ans = [0] * n  # Initialize the result list with zeros
        stack = []  # Stack to store indices of temperatures
        
        for i in range(n - 1, -1, -1):  # Traverse the list in reverse order
            # Pop elements from the stack that are less than or equal to the current temperature
            while stack and temp[stack[-1]] <= temp[i]:
                stack.pop()
            
            # If the stack is not empty, calculate the distance to the next warmer day
            if stack:
                ans[i] = stack[-1] - i
            
            # Push the current index onto the stack
            stack.append(i)
        
        return ans
