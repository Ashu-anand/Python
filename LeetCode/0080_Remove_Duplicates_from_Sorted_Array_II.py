from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt=1
        write_pointer=1
        duplicate_cnt=0
        for idx,val in enumerate(nums[1:]):
            if nums[idx]==val:
                nums[write_pointer]=val
                if cnt==1:
                    cnt+=1
                    write_pointer+=1
                else:
                    duplicate_cnt+=1
            else:
                nums[write_pointer]=val
                cnt=1
                write_pointer+=1
        return len(nums)-duplicate_cnt
s=Solution()
nums = [0,0,1,1,1,1,2,3,3]
print(s.removeDuplicates(nums))
