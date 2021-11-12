from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d={}
        for val in nums:
            if val in d:
                d[val]+=1
            else:
                d[val]=1
        cnt=1
        dup=0
        miss=0
        for idx in sorted(d.items(),key=lambda a:a[0]):
            if cnt!=idx[0]:
                miss=cnt
                cnt += 1
            if idx[1]>1:
                dup=idx[0]
            cnt+=1
        return [dup,miss]


s = Solution ()
nums = [1,1,2]
print (s.findErrorNums (nums))
