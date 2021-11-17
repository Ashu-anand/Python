class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        d={'1':1,'2':2,'3':3,
           '4':4,'5':5,'6':6,
           '7':7,'8':8,'9':9,'0':0}
        num1_len=len(num1)
        num2_len=len(num2)
        if num1_len>num2_len:
            num2='0'*(num1_len-num2_len)+num2
        else:
            num1='0'*(num2_len-num1_len)+num1
        idx=num1_len=num2_len=0
        while len(num1)>idx:
            num1_len=d[num1[idx]]+num1_len*10
            num2_len=d[num2[idx]]+num2_len*10
            idx+=1
        return str(num1_len*num2_len)
s = Solution ()
num1 = "123"
num2 = "456"
print (s.multiply (num1,num2))
