Question
n a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
Return the element repeated N times.

 

Example 1:
Input: [1,2,3,3]
Output: 3

Example 2:
Input: [2,1,2,5,3,2]
Output: 2

Example 3:
Input: [5,1,5,2,5,3,5,4]
Output: 5
 

Note:
4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even


PSEUDO CODE
1) Start with Index 1
2) Check if Index 0==1 or 1==2 then return 1
3) check if index 0==2 then return 0
4) update index =index+1 and repeat step 2 and 3
5) If nothing, check if index 0 equals to the last element and return value of index 0

Solution:
from typing import List
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        ans=0
        for idx,c in enumerate(A):
            for jdx in A[idx+1:]:
                if c==jdx:
                    return c
        return ans


s=Solution()
num=[5,1,5,2,5,3,5,4]
print(s.repeatedNTimes(num))


Solution: 2
from typing import List
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        if A[0]==A[len(A)-1]:return A[0]
        left=1
        while(left<len(A)-1):
            if A[left-1]==A[left] or A[left]==A[left+1]:
                return A[left]
            elif A[left-1]==A[left+1]:
                return A[left-1]
            left +=1
