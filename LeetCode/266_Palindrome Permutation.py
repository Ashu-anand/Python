from typing import List
from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnt=Counter(s)
        c=0
        for idx,val in cnt.items():
            if val%2!=0:
                c+=1
        return True if c<2 else False

s=Solution()
txt='aa'
print(s.canPermutePalindrome(txt))