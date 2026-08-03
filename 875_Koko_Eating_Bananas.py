class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            time = 0
            middle = (left + right) // 2
            for pile in piles:
                time += ((pile + middle - 1) // middle)
            if time <= h:
                right = middle
            elif time > h:
                left = middle + 1
        return right