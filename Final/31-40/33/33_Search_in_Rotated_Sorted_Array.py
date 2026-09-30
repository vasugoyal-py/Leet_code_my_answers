class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while r >= l:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] > target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
        return - 1