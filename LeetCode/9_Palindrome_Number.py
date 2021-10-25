class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        s=str(x)
        left,right=0,len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return False
            else:
                left+=1
                right-=1
        return True


s=Solution()
txt= [121,-121,10,-101]
for i in txt:
    print(i, s.romanToInt(i))
