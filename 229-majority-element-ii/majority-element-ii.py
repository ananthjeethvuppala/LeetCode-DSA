class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return []

        cand1 = None
        cand2 = None
        count1 = 0
        count2 = 0 

        for num in nums:

            if num == cand1:
                count1 += 1

            elif num == cand2:
                count2 += 1

            elif count1 == 0:
                count1 = 1
                cand1 = num

            elif count2 == 0:
                count2 = 1
                cand2 = num

            else:
                count1 -= 1
                count2 -= 1

        res = []
        n = len(nums)
        if nums.count(cand1) > n // 3:
            res.append(cand1)
        if cand1 != cand2 and nums.count(cand2) > n//3:
            res.append(cand2)
        
        return res