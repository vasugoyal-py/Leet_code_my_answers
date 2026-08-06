class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        leng = len(s)
        answer = 0
        for i in range(leng):
            if s[i] in dic:
                while dic:
                    ket = next(iter(dic))
                    dic.pop(ket)

                    if ket == s[i]:
                        break

            dic[s[i]] = i
            answer = max(answer, len(dic))
        return answer