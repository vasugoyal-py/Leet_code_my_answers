class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = str(x)[::-1]
        real = str(x)

        if real == reverse:
            return True
        else:
            return False