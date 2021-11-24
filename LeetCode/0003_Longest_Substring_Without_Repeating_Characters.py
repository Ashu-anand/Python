from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        if len(s)<2: return len(s)
        length=len(s)
        right=1
        left=0
        ans=0
        d={}
        d[s[left]]=left
        while right<length:
            if s[left]!=s[right]:
                if s[right] not in d:
                    d[s[right]]=right
                    right+=1
                else:
                    if d[s[right]]>left:
                        left=d[s[right]]+1
                        d[s[right]]=right
                        right+=1
                    else:
                        d[s[right]]=right
                        right+=1
            else:
                d[s[left]]=right
                right+=1
                left+=1
            ans=max(ans,right-left)
        return ans
s=Solution()
text = "pwwkew"
print(s.lengthOfLongestSubstring(text))