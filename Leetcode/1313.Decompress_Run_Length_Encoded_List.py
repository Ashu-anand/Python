Question
We are given a list nums of integers representing a list compressed with run-length encoding.
Consider each adjacent pair of elements [a, b] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, 
there are a elements with value b in the decompressed list.
Return the decompressed list.

Example 1:
Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4,4] is [2,4,4,4].
 

Constraints:
2 <= nums.length <= 100
nums.length % 2 == 0
1 <= nums[i] <= 100




PSEUDO CODE
1) Take the first number and repeat the second number first time
2) Increase the count of the For Loop by 2 and repeat the first step
3) Add all the ans and return the same




Code:
from typing import List
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(0,len(nums),2):
            a=[nums[i+1]]*nums[i]
            ans=ans+a
        return ans


s=Solution()
num= [1,2,3,4,5,8]
print(s.decompressRLElist(num))
