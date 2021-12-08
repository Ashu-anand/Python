from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d={}
        for val in arr:
            if val*2 in d or val/2 in d:
                return True
            else:
                d[val]=None
        return False
s=Solution()
nums = [10,2,5,3]
print(s.checkIfExist(nums))
