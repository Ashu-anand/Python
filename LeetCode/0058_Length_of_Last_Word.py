class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # First we will remove the extra spaces at the end of the string by using strip function
        # Second we can split the words into an list to get the last word
        # At last by using -1 index we can get the last word to find the length
        return len(s.strip().split()[-1])


s = Solution ()
S = "   fly me   to   the moon  "
print (s.lengthOfLastWord(S))