from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        left=1
        right=len(nums)

        while left<right:
            nums.insert(left,nums.pop())
            left+=2
        return nums
                

s=Solution()
nums = [1,3,2,2,3,1]
print(s.wiggleSort(nums))
