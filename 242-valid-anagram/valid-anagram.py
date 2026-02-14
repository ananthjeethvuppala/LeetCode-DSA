class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        elif Counter(s) == Counter(t):
            return True
        else:
            return False
        