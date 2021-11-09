from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a=0
        while True:
            try:
                nums.remove(val)
                nums.append('_')
                a+=1
            except:
                return len(nums)-a

s=Solution()
nums = [3,2,2,3]
val = 3
print(s.removeElement(nums,val))
