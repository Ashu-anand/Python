class Solution:
    def hammingWeight(self, n: int) -> int:
        return len(bin(n).replace('0','')[1:])

s=Solution()
n = 11
print(s.hammingWeight(n))