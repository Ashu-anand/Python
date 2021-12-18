from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ans=[]
        def add_val(val,i):
            ans.append(val[i])
            return i+1
        n=len(nums)
        if n<=1:
            return nums
        mid=n//2
        left=self.sortArray(nums[:mid])
        right=self.sortArray(nums[mid:])
        idx=0
        jdx=0
        while idx<len(left) and jdx<len(right):
            if left[idx]==right[jdx]:
                idx=add_val(left,idx)
                jdx=add_val(right,jdx)
            elif left[idx]>right[jdx]:
                jdx=add_val(right,jdx)
            else:
                idx=add_val(left,idx)
        if idx==len(left):
            while jdx<len(right):
                jdx=add_val(right,jdx)                
        else:
            while idx<len(left):
                idx=add_val(left,idx)
        return ans

s=Solution()
nums = [5,1,1,2,0,0]
print(s.sortArray(nums))
