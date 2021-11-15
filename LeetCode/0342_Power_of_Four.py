class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1: return True
        if n%2==1 or n==0: return False
        while True:
            n=n/4
            if n!=int(n):
                return False
            if n==1: return True
        return ans
        
       
s=Solution()
nums=128
print(s.isPowerOfFour(nums))