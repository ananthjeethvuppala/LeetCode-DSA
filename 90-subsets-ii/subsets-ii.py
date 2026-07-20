class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        path = []

        def solve(index):

            ans.append(path.copy())

            for i in range(index, len(nums)):

                if i > index and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])

                solve(i+1)

                path.pop()
            
        solve(0)

        return ans
