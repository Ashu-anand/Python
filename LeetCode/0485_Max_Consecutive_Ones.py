from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        temp=0
        for val in nums:
            if val==1:
                temp+=1
            else:
                ans=max(ans,temp)
                temp=0
        ans=max(ans,temp)
        return ans

s=Solution()
nums = [1,0,1,1,0,1]
print(s.findMaxConsecutiveOnes(nums))
