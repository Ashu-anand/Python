class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s=''
        while columnNumber>0:
            if columnNumber<=26:
                s = chr (64 + columnNumber) + s
                columnNumber=0
            else:
                temp=columnNumber%26
                if temp==0:
                    s='Z'+s
                    columnNumber-=1
                else:
                    s=chr(64+temp)+s
            columnNumber=columnNumber//26
        return s


s = Solution ()
columnNumber = 704
print (s.convertToTitle(columnNumber))