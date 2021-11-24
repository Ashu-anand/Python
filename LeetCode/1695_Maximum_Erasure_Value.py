from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans=0
        max_ans=0
        left=right=0
        d={}
        while right<(len(nums)):
            temp=nums[right]
            if temp not in d:
                d[temp]=temp
                ans+=temp
                right+=1
                max_ans=max(max_ans,ans)
            else:
                ans-=d.pop(nums[left])
                max_ans=max(max_ans,ans)
                left+=1
        return max_ans
s=Solution()
text = [4,2,4,5,6]
print(s.maximumUniqueSubarray(text))