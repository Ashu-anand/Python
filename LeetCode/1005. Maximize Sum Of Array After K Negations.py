from typing import List
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        if len(nums)==0: return 0
        if k==0: return sum(nums)
        nums.sort()
        idx=0
        while k>0 and idx<len(nums):
            if nums[idx]<0:
                nums[idx]=abs(nums[idx])
                idx+=1
                k-=1
            elif nums[idx]==0:
                return sum(nums)
            else:
                break
        m=min(nums)
        if k%2!=0:            
            return sum(nums)-(2*m)
        else:
            return sum(nums)

s=Solution()
num=[4,2,3]
k=1
print(s.largestSumAfterKNegations(num,k))