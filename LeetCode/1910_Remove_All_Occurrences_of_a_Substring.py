class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        l=0
        while l!=len(s):
            l=len(s)
            s=s.replace(part,'',1)
        return s

s=Solution()
txt = "daabcbaabcbc"
part = "abc"
print(s.removeOccurrences(txt,part))