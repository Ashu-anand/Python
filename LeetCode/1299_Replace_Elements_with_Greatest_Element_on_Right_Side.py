from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length=len(arr)-1
        pre_val=-1
        for idx in range(length-1,-1,-1):
            arr[idx],pre_val= max(arr[idx+1],pre_val),arr[idx]
        arr[-1]=-1
        return arr


s=Solution()
nums = [17,18,5,4,6,1]
print(s.replaceElements(nums))
