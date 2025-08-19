from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        

        if len1 > len2:
            return False

        count1 = Counter(s1)
        window = Counter(s2[:len1])

        if count1 == window:
            return True

        for i in range(len1,len2):
            window[s2[i]] += 1
            window[s2[i - len1]] -= 1

            if count1 == window:
                return True
        return False
        