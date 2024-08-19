class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # count = 0
        # for i in s2:
        #     if i in s1:
        #         count += 1
        #         if count == len(s1):
        #             return True
        #     else:
        #         count = 0
        # return False
        l = 0 
        s1 = sorted(s1)
        for r in range(len(s1),len(s2)+1):
            x = s2[l:r]
            x = sorted(x)
            if x == s1:
                return True
            l+= 1
        return False


