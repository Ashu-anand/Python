from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i=0
        for idx,val in enumerate(nums[1:]):
            if nums[i]!=val:
                i+=1
                nums[i]=val
        return i+1


s=Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums))
