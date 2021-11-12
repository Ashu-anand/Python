class Solution:
    def helper(self,nums):
        n=0
        while nums>=9:
            n=n+nums%10
            nums=nums//10
        n+=nums
        return n

    def getLucky(self, s: str, k: int) -> int:
        num=int(''.join(str(ord(x)-96) for x in s))
        idx=0
        while idx<k:
            num=self.helper(num)
            idx+=1
        return num

s=Solution()
txt='leetcode'
k=2
print(s.getLucky(txt,2))