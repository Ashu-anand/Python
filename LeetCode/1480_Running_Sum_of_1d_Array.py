from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for idx,val in enumerate(nums[1:]):
            nums[idx+1]=nums[idx]+nums[idx+1]
        return nums

s=Solution()
nums = [1,2,3,4]
print(s.runningSum(nums))