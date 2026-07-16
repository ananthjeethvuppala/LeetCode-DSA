class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        num = 0

        while i<n and s[i] == ' ':
            i += 1
        
        while i<n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

            if i>=n or not s[i].isdigit():
                return 0



        while i<n and s[i].isdigit():
            num = num*10 + int(s[i])
            i += 1
        
        num *= sign

        INT_MIN = -2147483648
        INT_MAX = 2147483647

        if num > INT_MAX:
            return INT_MAX
        
        if num < INT_MIN:
            return INT_MIN
        
        return num
