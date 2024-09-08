class Solution:
    def __init__(self):
        # Initialize memoization dictionary with base cases
        self.memo = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        for i in range(3,n+1):
            if i in self.memo:
                return self.memo[i]

            # Recursive call with memoization
            result = self.memo[i - 1] + self.memo[i - 2]
            self.memo[i] = result  # Store the result for future reference
        return self.memo[n]
