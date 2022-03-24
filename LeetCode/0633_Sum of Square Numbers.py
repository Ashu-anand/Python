from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c<=1: return True
        for val in range(1,c):
            ans=c-(val*val)
            if ans<0:
                return False
            if sqrt(ans)==int(sqrt(ans)):
                return True

s=Solution()
n=4096
print(s.judgeSquareSum(n))