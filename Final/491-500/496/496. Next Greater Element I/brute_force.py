class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sol = []
        for i in nums1:
            le = len(sol)
            for j in range(nums2.index(i) + 1, len(nums2)):
                if i < nums2[j]:
                    sol.append(nums2[j])
                    break
            if le == len(sol):
                sol.append(-1)
        return sol