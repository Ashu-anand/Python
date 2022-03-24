class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1: return True
        left=2
        while left*left<num:
            left+=1
        return True if left*left==num else False
            
        

s=Solution()
n=4096
print(s.isPerfectSquare(n))