from typing import List
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines=1
        pixel=100
        for val in s:
            w=widths[ord(val)-97]
            if pixel-w< 0:
                pixel=100
                lines+=1
            pixel=pixel-w
                
        return [lines,100-pixel]

s=Solution()
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
strg = ""
print(s.numberOfLines(widths,strg))
