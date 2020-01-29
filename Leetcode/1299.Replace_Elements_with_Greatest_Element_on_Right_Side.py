Question
Given an array arr, replace every element in that array with the greatest element among the elements
to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5


PSEUDO CODE
1) make a new array with [-1]
2) start with the end of the old array and go towards left till we find the number bigger then end number.
	2.1) If the old number is bigger then new number then increase the count
	2.2) else, append the new number multiply by count to ans and old=new and cnt=1
3) append the new number multiply by count-1
4) Return ans[::-1]


Solution:
from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)==1: return [-1]
        ans=[-1]
        cnt=1
        big=arr[-1]
        for idx in arr[len(arr)-2::-1]:
            if big>idx:
                cnt =cnt+1
            else:
                ans=ans+[big]*cnt
                big=idx
                cnt=1
        ans=ans+[big]*(cnt-1)
        return ans[::-1]
s=Solution()
num=[17,18,5,4,6,1]
print(s.replaceElements(num))
