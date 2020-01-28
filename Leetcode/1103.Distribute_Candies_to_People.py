Question
We distribute some number of candies, to a row of n = num_people people in the following way:
We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n 
candies to the last person.
Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to
the second person, and so on until we give 2 * n candies to the last person.
This process repeats (with us giving one more candy each time, and moving to the start of the row after
we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).
Return an array (of length num_people and sum candies) that represents the final distribution of candies.

 

Example 1:

Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
Example 2:

Input: candies = 10, num_people = 3
Output: [5,2,3]
Explanation: 
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].
 

Constraints:

1 <= candies <= 10^9
1 <= num_people <= 1000

PSEUDO CODE
1) Make an empty array of number of people
2) Loop while candies becomes zero
	2.1) Take a variable of candies_running_total=1
	2.2) Open a loop for number of people for i =num_people
		2.2.1)	if candies_running_total < candies
			2.2.1.1)if yes, ans[i]=ans[i]+candies_running_total
			2.2.1.2)else, ans[i]=ans[i]+candies
					2.2.1.2.1) candies=candies-idx and break
			2.2.1.3) candies=candies-idx and idx=idx+1



Code:
Solution: 1
import time as t
from typing import List
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans=[0]*num_people
        idx=1
        while candies>0:
            for i in range(num_people):
                if idx<=candies:
                    ans[i]=ans[i]+idx
                else:
                    ans[i] = ans[i] + candies
                    candies = candies - idx
                    break
                candies = candies-idx
                idx +=1
        return ans

    def distributeCandies2(self, candies: int, num_people: int) -> List[int]:
        temp=n= num_people*(num_people+1)//2
        idx = 1 if candies>n else 0
        while candies>n:
            temp=temp+num_people**2
            if n+temp>=candies:
                break
            else:
                n=n+temp
                idx+=1
        ans=[(((idx*(idx+1))//2)*num_people)-(idx*(num_people-i-1)) for i in range(num_people)]
        candies=candies-sum(ans)
        temp=num_people*idx
        idx=0
        while candies>0:
            if candies >temp+idx+1:
                ans[idx] = ans[idx] + temp+idx+1
                candies = candies - (temp+idx+1)
            else:
                ans[idx] = ans[idx] + candies
                candies = candies - candies
                break
            idx=idx+1
        return ans


s=Solution()
num=14
t1=t.time()
print(s.distributeCandies(num,4))
print(t.time()-t1)
t1=t.time()
print(s.distributeCandies2(num,4))
print(t.time()-t1)

