from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost): return -1
        start_station=0
        idx=0
        tank=0
        while start_station<len(gas)-1:
            tank=tank+gas[idx]-cost[idx]
            if tank>=0:
                idx+=1
                if idx==len(gas):
                    idx=0
                if start_station==idx:
                    break
            else:
                tank=0
                idx+=1
                start_station=idx
        return start_station if tank>=0 else -1
s=Solution()
gas =  [5,1,2,3,4]
cost = [4,4,1,5,1]
print(s.canCompleteCircuit(gas,cost))
