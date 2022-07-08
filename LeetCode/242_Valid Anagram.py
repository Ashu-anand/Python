from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_txt=Counter(s)
        t_txt=Counter(t)
        for idx,val in s_txt.items():
            if t_txt[idx]==val:
                t_txt.pop(idx)
            else:
                return False
        for idx,val in t_txt.items():
            return False
        return True
        