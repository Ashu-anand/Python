# This question is exactly similar to Leetcode question number 121.
# Only difference of return -1 instead of 0, hence i have copied the code.
from typing import List
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # Take the max diff as -1
        max_diff = -1
        # First num
        num = nums[0]
        # Open the loop to check each num
        for val in nums:
            # If the previous num  is greater then current, then
            # we will take current as new num
            if num >= val:
                num = val
            # As previous num is less than current num then this is diff.
            # If the diff is more than max diff, save this diff else continue with old max diff.
            else:
                temp = val - num
                if temp > max_diff:
                    max_diff = temp
        return max_diff


s = Solution ()
prices = [7,6,4,3,1]
print (s.maximumDifference(prices))