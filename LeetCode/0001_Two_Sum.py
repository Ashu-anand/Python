from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={nums[0]:0}
        for idx,val in enumerate(nums[1:]):
            if target-val in d:
                return [d[target-val],idx+1]
            else:
                d[val]=idx+1

s=Solution()
nums = [2,7,11,15]
target = 9
print(s.twoSum(nums,target))