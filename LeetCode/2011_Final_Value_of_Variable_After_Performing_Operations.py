from typing import List
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans=0
        for val in operations:
            if val[1]== '+':
                ans+=1
            else:
                ans-=1
        return ans

s=Solution()
operations = ["--X","X++","X++"]
print(s.finalValueAfterOperations(operations))