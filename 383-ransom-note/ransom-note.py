from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magzine_count = Counter(magazine)
        ransome_count = Counter(ransomNote)

        for char,freq in ransome_count.items():
            if magzine_count[char] < freq:
                return False
        return True