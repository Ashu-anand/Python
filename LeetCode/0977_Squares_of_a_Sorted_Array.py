from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return [nums[0]*nums[0]]
        left=0
        right=len(nums)-1
        ans=[0]*len(nums)
        while left<=right:
            if abs(nums[left])<=abs(nums[right]):
                temp=nums[right]*nums[right]
                ans[right-left]=temp
                right-=1
            else:
                temp=nums[left]*nums[left]
                ans[right-left]=temp
                left+=1            
        return ans


s=Solution()
nums =[-8,-6,-4,-3,0]
print(s.sortedSquares(nums))
