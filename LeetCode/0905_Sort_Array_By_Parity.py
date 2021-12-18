from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        rp=1
        wp=0
        while rp<len(nums):
            if nums[wp]%2==0:
                wp+=1
            elif nums[rp]%2==0:
                nums[wp],nums[rp]=nums[rp],nums[wp]
                wp+=1
            rp+=1
        return nums

s=Solution()
nums = [3,1,2,1,0,4]
print(s.sortArrayByParity(nums))
