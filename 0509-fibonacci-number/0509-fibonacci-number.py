#Solution without memoization
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n<=2 :
#             return 1
#         result = self.fib(n-1)+self.fib(n-2)
#         return result


#Solution with memoization
# class Solution:
#     def __init__(self):
#         self.memo = {}
#     def fib(self, n: int) -> int:
#         if n in self.memo:
#             return self.memo[n]
#         if n == 0:
#             return 0
#         if n<=2 :
#             return 1
#         result = self.fib(n-1)+self.fib(n-2)
#         self.memo[n] = result
#         return result
        


#improve memoization approach

class Solution:
    def __init__(self):
        self.memo = {1: 1, 2: 1,0:0}  # Base cases

    def fib(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]  # Return cached result
        
        # Calculate Fibonacci iteratively and store in memo
        for i in range(3, n + 1):
            self.memo[i] = self.memo[i - 1] + self.memo[i - 2]
        
        return self.memo[n]
