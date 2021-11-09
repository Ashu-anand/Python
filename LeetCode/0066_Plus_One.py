from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Get the length of the list as it will be require for inserting one extra number
        l=len(digits)-1
        while True:
            # if last digit is not 9 then it means only increase by 1 and return
            if digits[l]!=9:
                digits[l]+=1
                return digits
            # if the last digit is 9 which means we need to make this as 0 and 1 will be carry over.
            # in the next pass if the next digit is less than 9 then just increase else continue
            else:
                digits[l]=0
                l-=1
            # if the next field is not there then we need to insert and stop
            if l==-1:
                digits.insert(0,1)
                return  digits



s = Solution ()
digits = [4,3,2,1]
print (s.plusOne(digits))