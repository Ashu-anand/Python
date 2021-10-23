class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,
           'V':5,
           'X':10,
           'L':50,
           'C':100,
           'D':500,
           'M':1000}
        ans=0
        tmp1=0
        for idx in s:
            tmp2=d[idx]
            if tmp1<tmp2:
                ans=ans-tmp1 + (tmp2-tmp1)
                tmp1=tmp2
            else:
                ans=ans+tmp2
                tmp1 = tmp2
        return ans

s=Solution()
txt= ['III','IV','IX','LVIII','MCMXCIV']
for i in txt:
    print(i, s.romanToInt(i))