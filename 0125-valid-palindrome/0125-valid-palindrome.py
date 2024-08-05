class Solution:
    def isPalindrome(self, s: str) -> bool:
        # x = ''.join(char for char in s if char.isalnum())
        x = []
        for char in s :
            if char.isalnum():
                x.append(char)
        x = "".join(x)
        x = x.lower()
        return x == x[::-1]
        
        # l = 0
        # r = len(x)-1
        # while l < r :
        #     if x[l] != x[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True

