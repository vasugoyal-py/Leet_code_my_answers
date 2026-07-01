class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float('inf')
        max_p = 0 
        for i in prices:
            if min > i:
                min = i
            current_profit = i - min
            if max_p < current_profit:
                max_p = current_profit
        return max_p
             