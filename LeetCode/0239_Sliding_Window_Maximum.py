from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque(nums[:k])
        max_num=max(window)
        ans=[max_num]
        for i in range(k,len(nums)):
            old_num=window.popleft()
            next_num=nums[i]
            window.append(next_num)
            if max_num<=next_num:
                max_num=next_num
            else:
                if max_num==old_num:
                    max_num=max(window)
            ans.append(max_num)
        return ans
s = Solution ()
nums=[1,3,1,2,0,5]
k=3
print (s.maxSlidingWindow (nums, k))
