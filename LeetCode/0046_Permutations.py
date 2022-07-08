from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        if len(nums)==2:
            return [nums,[nums[1],nums[0]]]
        if len(nums)==1:
            return [nums]
        for idx,val in enumerate(nums):
            temp=self.permute(nums[:idx]+nums[idx+1:])
            for x in temp:
                x.insert(0,val)
                ans.append(x)
        return ans


import time
nums=[1,2,3,4,5,6,7,8,9,10]
s=Solution()
start_time = time.time()
Kavyansh=s.permute(nums)
print("--- %s seconds ---" % (time.time() - start_time))
