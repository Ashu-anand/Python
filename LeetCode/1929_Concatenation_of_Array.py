from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums

s=Solution()
nums = [1,2,1]
print(s.getConcatenation(nums))