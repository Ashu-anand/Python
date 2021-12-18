from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        wp=0
        while wp<len(nums):
            temp=nums[wp]
            if nums[wp]==wp+1 or nums[temp-1]==temp:
                wp+=1
            else:
                nums[wp]=nums[temp-1]
                nums[temp-1]=temp
        ans=[]
        for idx,val in enumerate(nums):
            if val!=idx+1:
                ans.append(idx+1)
        return ans
s=Solution()
nums = [4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(nums))
