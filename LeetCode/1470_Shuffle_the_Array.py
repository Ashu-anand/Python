from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        idx=0
        while idx<n-1:
            nums.insert(2*idx+1,nums.pop(idx+n))
            idx+=1
        return nums

s=Solution()
nums = [2,5,1,3,4,7]
n = 3
print(s.shuffle(nums,n))