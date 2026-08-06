class Solution:
    def reverse(self, x: int) -> int:
        new = str(x)
        rev = new[::-1]
        if new[0] == '-':
            rev = '-' + rev[:-1]

        irev = int(rev)

        if irev < -(2**31) or irev > (2**31-1):
            return 0
        else:
            return irev