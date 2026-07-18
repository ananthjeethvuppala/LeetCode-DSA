class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def solve(curr, opencount, closecount):

            if len(curr) == 2*n:
                ans.append(curr)
                return
            
            if opencount < n:
                solve(curr + '(', opencount + 1, closecount)
            
            if closecount < opencount:
                solve(curr + ')', opencount, closecount + 1)

        solve("", 0, 0)
        
        return ans
