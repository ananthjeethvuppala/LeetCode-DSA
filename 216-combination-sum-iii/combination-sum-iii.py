class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        ans = []

        def solve(start, currsum):
            if currsum == n and len(path) == k:
                ans.append(path.copy())
                return
            
            if currsum > n:
                return
            
            if len(path) > k:
                return

            for i in range(start, 10):

                path.append(i)

                solve(i + 1, currsum + i)

                path.pop()
        
        solve(1, 0)
        return ans