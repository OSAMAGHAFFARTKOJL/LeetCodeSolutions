class Solution:
    def isBalanced(self, num: str) -> bool:
        even_sum = 0
        odd_sum = 0
        length = len(num)
        for i in range(0,length,2):
            odd_sum += int(num[i])
            if (i+1) < length:
                even_sum += int(num[i+1]) if num[i] else 0
        print(even_sum,odd_sum)
        return even_sum == odd_sum

        