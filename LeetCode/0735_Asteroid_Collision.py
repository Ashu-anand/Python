from typing import List
from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        idx=0
        stack=deque()
        while idx<len(asteroids):
            if (stack==deque() or  (stack[-1]<0 and asteroids[idx]>0) or (stack[-1]<0 and asteroids[idx]<0) or (stack[-1]>0 and asteroids[idx]>0)):
                stack.append(asteroids[idx])
                idx+=1
            else:                
                if stack[-1]+asteroids[idx]==0:                    
                    stack.pop()
                    idx+=1
                elif stack[-1]< abs(asteroids[idx]):
                    stack.pop()
                else:
                    idx+=1
        return list(stack)

s=Solution()
asteroids = [1,1,-1,-2]
print(s.asteroidCollision(asteroids))
