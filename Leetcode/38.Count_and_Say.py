Question
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. 
You can do so recursively, in other words from the previous member read off the digits, 
counting the number of digits in groups of the same digit.
Note: Each term of the sequence of integers will be represented as a string.
 

Example 1:
Input: 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" 
which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".




PSEUDO CODE
1) For Loop for the number of times
2) For loop for the string
	2.1) Take the first character of the ans into a variable
	2.2) Check if the first character and new value of the loop is same
		2.2.1) If same then increase the counter
		2.2.2) Else, append the count along with old value into S
	2.3) Once loop finish append the final count along with old value
3) Copy this value to Ans
4) Retrun Ans



Code:
from typing import List
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1: return 1
        ans='11'
        st=ans
        for i in range(n-2):
            ans=st
            old=ans[0]
            cnt=0
            st=''
            for j in ans:
                if j==old:
                    cnt +=1
                else:
                    st=st+str(cnt)+old
                    old=j
                    cnt=1
            st=st+str(cnt)+old
        return st

s=Solution()
num=7
print(s.countAndSay(num))
