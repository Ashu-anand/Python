from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dt={}
        for idx,val in enumerate(nums):
            if val in dt:
                if idx-dt[val]<=k:
                    return True
            dt[val]=idx
        return False

s = Solution ()
nums = [1,2,3,1]
k = 3
print (s.containsNearbyDuplicate(nums,k))