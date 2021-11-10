class Solution:
    def titleToNumber(self, s: str) -> int:
        A = 64
        ans = 0
        for i in s:
            temp = ord (i) - A
            if temp == 26:
                temp == 0
            ans = (ans * 26) + temp
        return ans

s = Solution ()
columnTitle = "A"
print (s.titleToNumber (columnTitle))
