class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n*(n + 1)//2
        sums = sum(nums)
        return total - sums