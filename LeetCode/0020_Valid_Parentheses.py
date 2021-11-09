class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0: return False
        left=['(','{','[']
        d={'(':')',
           '{':'}',
           '[':']'
        }
        empty=[]
        for idx in s:
            if idx in left:
                empty.append(d[idx])
            else:
                if len(empty)==0 or empty.pop() != idx:
                    return False
        return True if len(empty)==0  else  False


s=Solution()
txt=["()","()[]{}","(]","([)]","{[]}",'((',']']
for i in txt:
    print(i, s.isValid(i))