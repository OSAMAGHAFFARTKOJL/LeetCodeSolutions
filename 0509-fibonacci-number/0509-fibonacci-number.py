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
class Solution:
    def __init__(self):
        self.memo = {}
    def fib(self, n: int) -> int:
        if n in self.memo:
            return memo[n]
        if n == 0:
            return 0
        if n<=2 :
            return 1
        result = self.fib(n-1)+self.fib(n-2)
        self.memo[n] = result
        return result
        