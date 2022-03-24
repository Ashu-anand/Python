from typing import List
class Solution:
    def capitalizeTitle(self, title: str) -> str:        
        ans=''
        for val in title.title().split(' '):
            if len(val)<3:
                val=val.lower()
            ans=ans+' '+val
        return ans.strip()

s=Solution()
title = "First leTTeR of EACH Word"
print(s.capitalizeTitle(title))