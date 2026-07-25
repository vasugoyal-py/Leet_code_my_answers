class Solution:
    def maxArea(self, height: List[int]) -> int:
        final = 0
        i = 0
        j = len(height) -1
        while i < j:
            l = height[i]
            r = height[j]
            width = j - i
            length = min(l,r)
            if final < (width*length):
                final = width*length
            if l > r:
                j -= 1
            elif l < r:
                i += 1
            else:
                i +=1
        return final