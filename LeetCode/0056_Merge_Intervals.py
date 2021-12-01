from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        idx=0
        while idx<len(intervals)-1:
            if intervals[idx][1]<intervals[idx+1][0]:
                idx+=1
            else:
                intervals[idx]=[intervals[idx][0],max(intervals[idx+1][1],intervals[idx][1])]
                intervals.pop(idx+1)
        return intervals
s=Solution()
intervals =[[1,4],[2,3]]
print(s.merge(intervals))