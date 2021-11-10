from typing import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[*s]
        a=''
        for i in l:
            if i.isalnum():
                a=a+i.lower()
        return a==a[::-1]

s = Solution ()
tst="A man, a plan, a canal: Panama"
print (s.isPalindrome(tst))