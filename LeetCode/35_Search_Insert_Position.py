from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)
        while left<right and right-left!=1:
            mid = (left + right) // 2
            if nums[mid]==target: return mid
            if nums[mid]<target:
                left = mid
            else:
                right = mid
        if nums[left]<target:
            return right
        else:
            return left

s = Solution ()
nums = [1,3,5,6]
target = 0
print (s.searchInsert(nums,target))