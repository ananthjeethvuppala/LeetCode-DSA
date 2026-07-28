class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        for num in nums:
            xor ^= num

        mask = xor & -xor

        x = 0
        y = 0

        for num in nums:
            if num & mask:
                x ^= num
            else:
                y ^= num
        
        return [x, y]