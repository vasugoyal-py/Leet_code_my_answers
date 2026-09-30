class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i, v in enumerate(temperatures):
            if not stack:
                stack.append(i)
            while stack and v > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans