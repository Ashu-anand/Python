class Solution:
    def addDigits(self, num: int) -> int:
        return (num-1)%9+1  if num!=0 else 0
        
s=Solution()
num=12552031545
print(s.addDigits(num))