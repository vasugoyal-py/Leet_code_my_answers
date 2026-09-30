class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greatelement = {}
        sol = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            greatelement[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        for j in range(len(nums1)):
            sol.append(greatelement[nums1[j]])

        return sol