from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pointer=0
        current_pointer=0
        len_nums=len(nums)
        while current_pointer<len_nums:
            if nums[current_pointer]!=0:
                if zero_pointer!=current_pointer:
                    nums[zero_pointer]=nums[current_pointer]
                zero_pointer+=1
            current_pointer+=1
        while zero_pointer<current_pointer:
            nums[zero_pointer]=0
            zero_pointer+=1
        return nums
s=Solution()
nums = [1,2]
print(s.moveZeroes(nums))
