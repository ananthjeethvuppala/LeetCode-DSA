class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        temp = None
        for num in nums:
            if count == 0:
                temp = num
            if count >= 0:
                if temp == num:
                    count += 1
                else:
                    count -= 1
        return temp