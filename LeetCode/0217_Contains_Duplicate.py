from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for val in nums:
            if val in hashmap:
                return True
            else:
                hashmap[val]=None
        return False


s = Solution ()
nums = [1,2,3,1]
print (s.containsDuplicate(nums))