class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []

        def solve(index, curr):

            if index == len(digits):
                ans.append(curr)
                return
            
            for ch in phone[digits[index]]:

                solve(index + 1, curr + ch)
            
        solve(0, "")
        return ans