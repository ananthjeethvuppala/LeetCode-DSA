from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        left = 0
        right = 0 
        formed = 0
        dict_t = Counter(t)
        required = len(dict_t)
        window = {}
        ans = float('inf'), None, None

        while right < len(s):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if char in dict_t and window[char] == dict_t[char]:
                formed += 1
            while left <= right and formed == required :
                char = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                window[char] -= 1
                if char in dict_t and window[char] < dict_t[char]:
                    formed -= 1
                left += 1
            right +=1
        
        return "" if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]


        