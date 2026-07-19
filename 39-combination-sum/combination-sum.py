class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        def solve(index, currsum):

            if currsum == target:
                ans.append(path.copy())
                return

            if index == len(candidates):
                return

            if currsum > target:
                return

            path.append(candidates[index])
            solve(index, currsum + candidates[index])
            path.pop()

            solve(index + 1, currsum)
        
        solve(0, 0)
        return ans