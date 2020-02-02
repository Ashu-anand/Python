Logic:
1) start from left to right and check if any 0 exists. If yes, skip
2) convert the number into string and loop through the number and divide each number. If a division result
   comes as non-zero, then do not add that number and break the loop
3) if the ans is zero for all the above cases, then add the result.


Solution:

from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for idx in range(left,right+1):
            if str (idx).count ('0') == 0:
                add=True
                for i in str(idx):
                    if idx%int(i)!=0:
                        add=False
                        break
                if add:
                    ans.append(idx)
        return ans
s=Solution()
left=1
right=10000
print(s.selfDividingNumbers(left,right))
