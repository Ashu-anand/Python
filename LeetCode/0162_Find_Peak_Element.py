from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def SearchPeak(nums,left,right):
            mid=(left+right)//2
            if left==right:
                return left
            if nums[mid]> nums[mid+1]:
                return SearchPeak(nums,left,mid)
            return SearchPeak(nums,mid+1,right)
        return SearchPeak(nums,0,len(nums)-1)

s=Solution()
nums = [1,2,1,3,5,6,4]
print(s.findPeakElement(nums))
