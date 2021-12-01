from typing import List
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries)==0: return 0
        ans = duration if timeSeries[0]==0 else 0
        previous_duration=0
        for val in timeSeries:
            ans = ans + duration - max (0,previous_duration-val+1)
            previous_duration=val+duration-1
        return ans

s=Solution()
timeSeries = [0,1,2,3,4,5]
duration = 1
print(s.findPoisonedDuration(timeSeries,duration))
