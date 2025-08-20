from collections import Counter 
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_dict = sorted(count.items(), key = lambda x:x[1], reverse = True)
        result = ""
        for char,freq in sorted_dict:
            result += char * freq
        return result