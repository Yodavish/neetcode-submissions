class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        for s_char in s:
            dic_s[s_char] = dic_s.get(s_char, 0) + 1

        for t_char in t:
            dic_t[t_char] = dic_t.get(t_char, 0) + 1
        
        return dic_s == dic_t
