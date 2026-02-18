class Solution(object):
    def maxDepth(self, s):
        md = 0 
        cd = 0

        for char in s:
            if char == "(":
                cd += 1
                md = max(cd,md)
            elif char == ")":
                cd -= 1
                md = max(cd,md)
        return md
        