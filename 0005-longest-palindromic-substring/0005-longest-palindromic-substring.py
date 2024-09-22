class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        for i in range(len(s)):
            l = i 
            r = i 
            
            while l >= 0 and r < len(s) and s[l:r+1] == s[l:r+1][::-1]:
                if len(res) < len(s[l:r+1]):
                    res = s[l:r+1]
                l -= 1
                r += 1
            
            l = i 
            r = i+1
            while l >= 0 and r < len(s) and s[l:r+1] == s[l:r+1][::-1]:
                if len(res) < len(s[l:r+1]):
                    res = s[l:r+1]
                l -= 1
                r += 1

        
        
        return res




            
        