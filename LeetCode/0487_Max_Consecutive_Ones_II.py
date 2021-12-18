from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        ans=[]
        for val in nums:
            if val==1:
                cnt+=1
            else:
                ans.append(cnt)
                ans.append(0)
                cnt=0
        ans.append (cnt)
        if len(ans)==1: return ans[0]
        temp=sum (ans[0:3])
        cnt=temp
        for idx, val in enumerate (ans[3:]):
            temp=temp + val - ans[idx]
            cnt = max (cnt, temp)
        return cnt+1
s=Solution()
nums = [1,0,1,1,0,1,1]
print(s.findMaxConsecutiveOnes(nums))
