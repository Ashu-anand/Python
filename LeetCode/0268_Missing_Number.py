from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length=len(nums)
        return ((length*(length+1))//2)-sum(nums)


s=Solution()
nums = [9,6,4,2,3,5,7,0,1]
print(s.missingNumber(nums))