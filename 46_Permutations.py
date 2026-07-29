class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        curr = []

        def recur():
            if len(curr) == n:
                ans.append(curr[:])
                return
            else:
                for x in nums:
                    if x not in curr:
                        curr.append(x)
                        recur()
                        curr.pop()
        recur()
        return ans