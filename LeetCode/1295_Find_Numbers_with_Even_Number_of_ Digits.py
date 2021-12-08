from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:        
        ans=0
        for val in nums:
            ans=ans + (1 if len(str(val))%2==0 else 0)
        return ans

s=Solution()
nums = [555,901,482,1771]
print(s.findNumbers(nums))
