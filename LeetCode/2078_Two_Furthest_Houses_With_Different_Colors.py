from typing import List
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        d={}
        for idx,val in enumerate(colors):
            if val in d:
                d[val][1]=idx
            else:
                d[val]=[idx,idx]
        max_distance=0
        for idx,val in d.items():
            for jdx,jal in d.items():
                if idx!=jdx:
                    max_distance=max(max_distance,abs(val[0]-jal[1]))
        return max_distance
s=Solution()
nums = [4,4,4,11,4,4,11,4,4,4,4,4]
print(s.maxDistance(nums))
