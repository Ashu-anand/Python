Question
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction 
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: 
	asteroids = [5, 10, -5]
	Output: [5, 10]
Explanation: 
	The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

Example 2:
Input: 
	asteroids = [8, -8]
	Output: []
Explanation: 
	The 8 and -8 collide exploding each other.

Example 3:
Input: 
	asteroids = [10, 2, -5]
	Output: [10]
Explanation: 
	The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.

Example 4:
Input: 
	asteroids = [-2, -1, 1, 2]
	Output: [-2, -1, 1, 2]
Explanation: 
	The -2 and -1 are moving left, while the 1 and 2 are moving right.
	Asteroids moving the same direction never meet, so no asteroids will meet each other.

Note:
The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000].



PSEUDO CODE
1) Start with the End and check if index <0 <index-1. If the index is less than 0 and index-1 is greater then 0 then they will collide
2) if no, then index=index-1
3) if yes, then
	3.1) Check if abs(index)==abs(index-1)
		3.1.1) if yes, then pop both
	3.2) Check if abs(index)== min(index,index-1)
		3.2.1) pop index
	3.3) else pop index-1
	3.4) if Index > length of the array, then Index=Length
	3.5) else nothing.
	
Solution:
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right=len (asteroids) - 1
        while right>0:
            if asteroids[right]<0 and asteroids[right-1]>0:
                if abs(asteroids[right])==abs(asteroids[right-1]):
                    asteroids.pop(right)
                    asteroids.pop (right-1)
                else:
                    if abs(asteroids[right])==min(abs(asteroids[right]),abs(asteroids[right-1])):
                        asteroids.pop(right)
                    else:
                        asteroids.pop (right-1)
                if right >= len (asteroids) - 1:
                    right = len (asteroids) - 1
            else:
                right=right-1
        return asteroids
s=Solution()
num=[-2,2,-1,-2]
num= [-2, -1, 1, 2]
print(s.asteroidCollision(num))
