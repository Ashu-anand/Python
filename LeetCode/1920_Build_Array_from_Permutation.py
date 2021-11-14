from typing import List
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        length=len(nums)
        for idx,val in enumerate(nums):
            temp=nums[val]
            if temp>idx:
                nums[idx]=val+(temp%length)*length
            else:
                t=temp%length
                nums[idx]=val+(t%length)*length
        for idx,val in  enumerate(nums):
            nums[idx]=val//length
        return nums
s=Solution()
nums = [0,2,1,5,3,4]
print(s.buildArray(nums))