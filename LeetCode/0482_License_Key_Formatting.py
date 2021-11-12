class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace('-','').upper()
        temp=len(s)%k
        if temp==0:
            ans=s[:k]
            temp=k
        else:
            ans=s[:temp]
        for idx,val in enumerate(s[temp:]):
            if (idx) % k==0:
                ans=ans+'-'            
            ans=ans+val
        return ans

s=Solution()
tst = "2-5g-3-J"
k = 2
print(s.licenseKeyFormatting(tst,k))