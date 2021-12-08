from typing import List
class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n<=1: return n
        nums=0
        idx=1
        while idx*idx<=n:
            nums+=1
            idx+=1
        return nums
                

s=Solution()
n = 12
print(s.bulbSwitch(n))
