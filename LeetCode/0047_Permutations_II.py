from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        def backtrack(first=0):
            if first==n:
                ans.add(tuple(nums[:]))
            for val in range(first,n):
                nums[first],nums[val]=nums[val],nums[first]
                backtrack(first+1)
                nums[first],nums[val]=nums[val],nums[first]

        n=len(nums)
        backtrack()
        ans=list(list(i) for i in ans)
        return ans

nums=[1,1,2]
s=Solution()
Kavyansh=s.permuteUnique(nums)
print(Kavyansh)
