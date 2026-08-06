class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("CM", "DCCCC")
        s = s.replace("CD", "CCCC")
        s = s.replace("XC", "LXXXX")
        s = s.replace("XL", "XXXX")
        s = s.replace("IX", "VIIII")
        s = s.replace("IV", "IIII")

        for dig in s:
            number += translations[dig]
        return number 