from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        idx=0
        left=0
        while idx<n:
            if nums[idx]==2:
                #nums.append(nums.pop(idx))
                temp=idx
                while temp<n-1:
                    nums[temp],nums[temp+1]=nums[temp+1],nums[temp]
                    temp+=1
                n-=1
            elif nums[idx]==0:
                #nums.insert(0,nums.pop(idx))
                temp=idx
                while temp>left:
                    nums[temp],nums[temp-1]=nums[temp-1],nums[temp]
                    temp-=1
                left+=1
                idx+=1
            else:
                idx+=1
        return nums

s=Solution()
nums = [2,0,2,1,1,0]
print(s.sortColors(nums))
