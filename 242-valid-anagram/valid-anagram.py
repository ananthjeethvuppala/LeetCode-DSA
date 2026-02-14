class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        elif sorted(s) == sorted(t):
            return True
        else:
            return False
        