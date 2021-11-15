from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_val=0
        for idx in accounts:
            max_val=max(max_val,sum(idx))
        return max_val
            
        
s=Solution()
accounts = [[1,2,3],[3,2,1]]
print(s.maximumWealth(accounts))