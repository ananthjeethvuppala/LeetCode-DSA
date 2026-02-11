class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            char = strs[0][i]

            for s in strs:
                if char != s[i]:
                    return s[:i]
        
        return strs[0][:min_len]
        