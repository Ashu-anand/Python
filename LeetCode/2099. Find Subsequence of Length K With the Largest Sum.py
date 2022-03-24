from typing import List
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums.sort(reverse=True)
        idx=0
        ans=0
        while k>0:
            if nums[idx]>=0:
                ans+=nums[idx]
                k-=1
                idx+=1
            else:
                break
        return ans
        
s=Solution()
nums=[2,1,3,3]
k=2
print(s.maxSubsequence(nums,k))