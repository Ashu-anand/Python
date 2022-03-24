from typing import List
class Solution:
    def twosum(self,nums,k,ans):
        d={}
        for i in nums:
            if i in d:
                l=tuple(sorted([k*-1,d[i],i]))
                if l not in ans:
                    ans.add(l)
            else:
                d[k-i]=i
        return ans
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        tested=set()
        for idx,val in enumerate(nums):
            if val not in tested:
                tested.add(val)
                ans= self.twosum(nums[:idx]+nums[idx+1:],val*-1,ans)            
        return ans

nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
s = Solution ()
print (s.threeSum(nums))