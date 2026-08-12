class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        for current in reversed(nums2):

            while stack and stack[-1] <= current:
                stack.pop()
            
            if stack:
                next_greater[current] = stack[-1]
            else:
                next_greater[current] = -1
            
            stack.append(current)
        
        return [next_greater[x] for x in nums1]