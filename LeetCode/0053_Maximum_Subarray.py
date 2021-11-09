from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for idx,val in enumerate(nums[1:]):
            if nums[idx]+val>val:
                nums[idx+1]=nums[idx]+val
        return sorted(nums)[-1]


s = Solution ()
nums = [-2,1]
print (s.maxSubArray(nums))