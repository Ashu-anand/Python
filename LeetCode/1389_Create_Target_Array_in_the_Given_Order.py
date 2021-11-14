from typing import List
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans=[]
        for idx,val in enumerate(nums):
            ans.insert(index[idx],nums[idx])
        return ans
s=Solution()
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(s.createTargetArray(nums,index))