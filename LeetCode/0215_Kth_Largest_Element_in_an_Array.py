from typing import List
from collections import Counter
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans=0
        c=Counter(nums)
        for val,idx in sorted(c.items(),reverse=True):
            k=k-idx
            if k<=0:
                return val



s=Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(s.findKthLargest(nums,k))
