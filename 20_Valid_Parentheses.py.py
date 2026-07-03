class Solution:
    def isValid(self, s: str) -> bool:
        lis = []
        poss = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        for i in s:
            if i in ['(', '{', '[']:
                lis.append(i)
            if i in poss:
                if not lis:
                    return False
                if poss[i] == lis[-1]: 
                    lis.pop()
                    continue
                else:
                    return False
        return not lis