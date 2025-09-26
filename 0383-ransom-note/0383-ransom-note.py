class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # The logic is to calculate the freq of each string and then check it
        count_ransomNote = Counter(ransomNote) # make a dict of counts
        count_magazine = Counter(magazine)
        print(count_ransomNote,count_magazine)
        for i in count_ransomNote:
            if i not in count_magazine:
                return False
            else:
                print(count_ransomNote[i],count_magazine[i])
                if count_ransomNote[i] > count_magazine[i]:
                    return False
        return True
        