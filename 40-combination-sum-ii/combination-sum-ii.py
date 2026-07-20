class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []
        path = []

        def solve(index, currsum):

            if currsum == target:
                ans.append(path.copy())
                return

            for i in range(index, len(candidates)):

                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                if currsum + candidates[i] > target:
                    break

                path.append(candidates[i])

                solve(i+1, currsum + candidates[i])

                path.pop()
        
        solve(0, 0)

        return ans