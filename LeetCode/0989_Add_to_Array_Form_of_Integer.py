from typing import List
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        if k==0: return num
        idx=len(num)-1
        while k>0:
            temp=k%10
            k=k//10
            if num[idx]+temp>9:
                num[idx]=(num[idx]+temp)%10
                k+=1
            else:
                num[idx]=num[idx]+temp
            idx-=1
            if idx<=0 and k!=0:
                idx+=1
                num.insert(0,0)
        if num[0]==0:
            num.pop(0)
        return num

s = Solution ()
num1 = [0]
num2 = 23
print (s.addToArrayForm (num1,num2))
