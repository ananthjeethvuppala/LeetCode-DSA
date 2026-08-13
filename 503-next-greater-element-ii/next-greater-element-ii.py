class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        result = [-1] * n

        for i in range(2 * n-1, -1, -1):
            index = i % n
            current = nums[index]

            while stack and stack[-1] <= current:
                stack.pop()
            
            if stack:
                result[index] = stack[-1]
            stack.append(current)
        
        return result