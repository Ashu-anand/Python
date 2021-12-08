from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()        
        for idx in range(len(nums),2,-1):
            val=nums[idx-3]+nums[idx-2]
            if val>nums[idx-1]:
                return val+nums[idx-1]
        return 0

s=Solution()
nums = [3,6,2,3]
print(s.largestPerimeter(nums))
