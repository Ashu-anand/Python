from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        len_num=len(nums)
        min_num=0
        i=0
        while i<len_num:
            if nums[i]==i+1:
                if min_num==i:
                    min_num+=1
                i+=1
            else:
                if nums[i]>len_num or nums[i]<1 or nums[i]==nums[nums[i]-1]:
                    min_num=min(min_num,i)
                    i+=1
                else:
                    if nums[i]!=nums[nums[i]-1]:
                        a=nums[i]
                        b=nums[a-1]
                        nums[i],nums[a-1]=b,a
                        min_num,i=i,min_num                    
        return min_num+1
        

nums1 = [4,2,5,2,3]
obt=Solution()
print(obt.firstMissingPositive(nums1))
