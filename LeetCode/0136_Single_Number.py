from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap={}
        for val in nums:
            if val in hashmap:
                hashmap[val] +=1
            else:
                hashmap[val]=1
        for i in hashmap.items():
            if i[1]==1: return i[0]

s=Solution()
nums = [4,1,2,1,2]
print(s.singleNumber(nums))