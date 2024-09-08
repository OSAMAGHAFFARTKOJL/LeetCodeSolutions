from typing import List

class Solution:
    def __init__(self):
        self.memo = {}

    def mini(self, a, b):
        # Correctly handle None values
        if a is None:
            return b
        if b is None:
            return a
        return min(a, b)

    def coinChange(self, coins: List[int], m: int) -> int:
        # Check memoization dictionary
        if m in self.memo:
            return self.memo[m]

        # Base case
        if m == 0:
            return 0

        result = None
        # Try each coin and recurse
        for coin in coins:
            sub = m - coin
            if sub < 0:
                continue  # Skip invalid subproblems

            sub_result = self.coinChange(coins, sub)
            if sub_result != -1:  # Only consider valid subresults
                result = self.mini(result, sub_result + 1)

        # Store the result in memo and return it
        self.memo[m] = -1 if result is None else result
        return self.memo[m]
