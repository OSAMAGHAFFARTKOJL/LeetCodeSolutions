class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # count = 0
        # for i in s2:
        #     if i in s1:
        #         count += 1
        #         if count == len(s1):
        #             return True
        #     else:
        #         count = 0
        # return False
        # l = 0 
        # s1 = sorted(s1)
        # for r in range(len(s1),len(s2)+1):
        #     x = s2[l:r]
        #     x = sorted(x)
        #     if x == s1:
        #         return True
        #     l+= 1
        # return False



        len_s1 = len(s1)
        len_s2 = len(s2)
        
        if len_s1 > len_s2:
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:len_s1])
        
        if s1_count == window_count:
            return True
        
        for i in range(len_s1, len_s2):
            start_char = s2[i - len_s1]
            new_char = s2[i]
            
            window_count[new_char] += 1
            
            if window_count[start_char] == 1:
                del window_count[start_char]
            else:
                window_count[start_char] -= 1
            
            if window_count == s1_count:
                return True
        
        return False
