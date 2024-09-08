class Solution:
    def __init__(self):
        # Initialize memoization dictionary with base cases
        self.memo = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        # Check if the result is already in the memoization dictionary
        if n in self.memo:
            return self.memo[n]

        # Recursive call with memoization
        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.memo[n] = result  # Store the result for future reference
        return result
