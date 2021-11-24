from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack=[]
        for idx,val in enumerate(intervals):
            if newInterval[1]<val[0]:
                stack.append(newInterval)
                return stack+intervals[idx:]
            else:
                if val[1]< newInterval[0]:
                    stack.append(val)
                else:
                    newInterval=[min(val[0],newInterval[0]),max(val[1],newInterval[1])]
        stack.append(newInterval)
        return stack
s=Solution()
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(s.insert(intervals,newInterval))