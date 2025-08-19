class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        revhalf=0
        while x>revhalf:
            revhalf=revhalf*10 + x%10
            x//=10
        return x==revhalf or x==revhalf//10