class Solution:
    def solve(self, n):
        if n==1: return True
        ans=bin(n)[2:]
        if ans[0]=='1':
            s=set()
            for i in ans[1:]:
                s.add(i)
            if len(s)==1 and list(s)[0]=='0':
                return True
            else:
                return False
        else:
            return False

s=Solution()
n=11
print(s.solve(n),bin(n))