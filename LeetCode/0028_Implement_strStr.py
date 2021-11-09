class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length=len(needle)
        if length==0: return 0
        right=0
        while right<len(haystack):
            if haystack[right]==needle[0]:
                if haystack[right:right+length]==needle:
                    return right
            right+=1
        return -1


s = Solution ()
haystack = "mississippi"
needle = "issipi"
print (s.strStr(haystack,needle))