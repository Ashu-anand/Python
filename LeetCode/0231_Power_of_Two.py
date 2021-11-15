class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1: return True
        t=str(bin(n))[2:]
        st=set(t[1:])               
        if t[0]=='1' and len(st)==1 and st.pop()=='0':
            return True
        else:
            return False

       
s=Solution()
nums=128
print(s.isPowerOfTwo(nums))