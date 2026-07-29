class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sol = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            l = i + 1
            r = n - 1

            while r > l:
                current_sum = nums[i] + nums[l] + nums[r]

                if current_sum == 0:
                    sol.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif current_sum > 0:
                    r -= 1
                else:
                    l += 1
        return sol