class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] = -1
            else:
                freq[s[i]] = i
        for i in freq.values():
            if i != -1:
                return i
        return -1

