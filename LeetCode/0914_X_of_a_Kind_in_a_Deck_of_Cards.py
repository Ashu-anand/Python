from typing import List
import math
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d={}
        for i in deck:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        n=0
        if not d: return False
        for k, v in sorted(d.items(), key=lambda item: item[1]):
            if n==0:
                if v==1:
                    return False
                else:
                    n=v
            else:
                if v%n!=0:
                    n=math.gcd(v, n)
                    if n==1 or v%n!=0:
                        return False
        return True

s = Solution ()
deck = [1,1,1,2,2,2,3,3]
print (s.hasGroupsSizeX(deck))