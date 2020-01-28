Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.


Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
 

Constraints:

1 <= s.length <= 1000
s[i] = 'L' or 'R'




PSEUDO CODE
1) Start with the first index and check if it's R or L
2) If it's R, then mark the counter for R and start checking next number.
2.1) If R comes, then increase the counter
2.2) If L comes, then decrease the counter
2.3) When counter becomes 0, then count the length as 1
3) Repeat the step 1-2.3 for R and L




Code:
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans=0
        R=0
        L=0
        for i in s:
            if R==0 and L==0:
                ans +=1
                if i=='R':
                    R += 1
                else:
                    L +=1
            else:
                if R>0:
                    if i=='R':
                        R +=1
                    else:
                        R -= 1
                else:
                    if i=='L':
                        L +=1
                    else:
                        L -= 1
        return ans

s=Solution()
num='RLRRRLLRLL'
print(s.balancedStringSplit(num))
