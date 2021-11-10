from typing import List
class Solution:
    def isHappy(self, n: int) -> bool:
        d={n:None}
        while n!=1:
            ans=0
            while n!=0:
                temp=n%10
                ans=ans+temp*temp
                n=n//10
            if ans in d:
                return False
            else:
                d[ans]=None
            n=ans
        return True



s = Solution ()
n=9999999999999
print (s.isHappy(n))