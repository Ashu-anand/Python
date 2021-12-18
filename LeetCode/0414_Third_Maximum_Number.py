from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_finder=set(nums)
        temp=max(max_finder)
        if len(max_finder)<=2:
            return temp
        else:
            for idx in range(2):
                max_finder.remove(temp)
                temp=max(max_finder)
        return temp

s=Solution()
nums = [2,2,3,1]
print(s.thirdMax(nums))
