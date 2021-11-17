class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]

s = Solution ()
num1 = "11"
num2 = "1"
print (s.addBinary (num1,num2))
