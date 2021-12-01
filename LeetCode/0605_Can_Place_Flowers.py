from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(-1)
        flowerbed.insert(0,-1)
        ON=False
        for i in range(1,len(flowerbed)):
            if ON:
                if flowerbed[i]==1: 
                    return False
                else:
                    ON=False
            else:
                if flowerbed[i]==0:
                    if flowerbed[i+1]!=1:
                        ON=True
                        n-=1
                        if n<=0: return True
                else:
                    ON=True
        return True
s=Solution()
flowerbed = [0,1,0,0]
n = 1
print(s.canPlaceFlowers(flowerbed,n))
