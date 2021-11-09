from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0: return ''
        strs.sort(key=lambda a: len(a))
        prefix=''
        for idx,val in enumerate(strs[0]):
            for jdx in strs[1:]:
                if jdx[idx]!=val:
                    return prefix
            prefix = prefix + val
        return prefix


strss = ["flower","flow","flight"]
s=Solution()
print(s.longestCommonPrefix(strss))