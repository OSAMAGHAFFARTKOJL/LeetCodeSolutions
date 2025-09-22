class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # first lets create the dict
        freq = {}

        # now lets store the frequency of each element
        for i in s:
            if i in freq:
                freq[i] += 1
                if freq[i] == 2:
                    return i
            else:
                freq[i] = 1
        