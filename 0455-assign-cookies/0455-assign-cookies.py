class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j=0
        i=0
        count=0
        while i<len(g)and j <len(s):
            if g[i] <= s[j]:
                count+=1
                i+=1
                j+=1
            elif  g[i] > s[j]:
                j+=1
        return count

        