from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        for val in nums:
            if val in hashmap:
                hashmap[val]+=1
            else:
                hashmap[val] = 1
        return sorted(hashmap.items(),key=lambda a:a[1],reverse=True)[0][0]

s = Solution ()
nums = [2,2,2,2,2,2,2,2,1,3,4,5,6,7,8,9,6]
print (s.majorityElement(nums))