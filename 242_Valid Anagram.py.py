class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dics = {}

        if len(s) != len(t):
            return False
        
        for i in s:
            if i in dics:
                dics[i] += 1
            else:
                dics[i] = 1

        for i in t:
            if i in dics:
                dics[i] -= 1
            else:
                return False

        if all(x == 0 for x in dics.values()):
            return True
        else:
            return False
        