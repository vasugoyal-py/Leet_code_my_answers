class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        best = 0
        for i in accounts:
            welth = sum(i)
            best = max(welth, best)
        return best