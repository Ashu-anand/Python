from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for idx in nums:
            if nums[abs(idx)]<0:
                for jdx in nums:
                    nums[abs(jdx)]=abs(nums[jdx])
                return abs(idx)
            else:
                nums[idx]=-1*(nums[idx])


s=Solution()
nums = [1,3,4,2,2]

print(s.findDuplicate(nums))