class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = prices.copy()  
        stack = [] 

        for i, value in enumerate(prices):
            while stack and prices[stack[-1]] >= value:
                j = stack.pop()
                ans[j] = prices[j] - value
            stack.append(i)

        return ans