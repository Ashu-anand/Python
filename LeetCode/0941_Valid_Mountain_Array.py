from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length=len(arr)
        if length<3: return False
        increasing=True
        for idx,val in enumerate(arr[1:]):            
            if arr[idx]<val:
                if not increasing:
                    return increasing            
            elif arr[idx]>val:
                if idx!=0:
                    increasing=False
                else:
                    return False
            elif arr[idx]==val: 
                return False
        return not increasing