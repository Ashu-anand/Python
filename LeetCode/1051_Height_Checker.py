from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_heights=sorted(heights)
        ans=0
        for idx,jdx in zip(heights,new_heights):
            if idx!=jdx:
                ans+=1
        return ans

s=Solution()
nums = [1,1,4,2,1,3]
print(s.heightChecker(nums))
