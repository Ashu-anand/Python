from typing import List
class Solution:    
    def duplicateZeros(self, arr: List[int]) -> None:
        def helper(LENGTH,val):
            arr[LENGTH]=val
            return LENGTH-1
            
        num_of_zeros=0
        idx=0
        while (idx+num_of_zeros)<len(arr):
            if arr[idx]==0:
                num_of_zeros+=1
            idx+=1
        idx-=1
        LENGTH=len(arr)-1
        if idx+num_of_zeros==LENGTH+1:
            LENGTH=helper(LENGTH,arr[idx])
            idx-=1
        while LENGTH!=idx:
            if arr[idx]==0:
                for i in range(2):
                    LENGTH=helper(LENGTH,0)                    
            else:
                LENGTH=helper(LENGTH,arr[idx])
            idx-=1
        return arr
s=Solution()
nums= [1,0,2,3,0,4,5,0]
print(s.duplicateZeros(nums))
