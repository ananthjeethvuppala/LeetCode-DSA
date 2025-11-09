class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longest = 0
        length = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                longest = 1
                current = num

                while current + 1 in nums_set:
                    longest += 1
                    current += 1
            
            length = max(length, longest)

        return length