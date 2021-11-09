from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Take the max profit as 0
        max_profit=0
        # First Day price as buy price
        buy=prices[0]
        # Open the loop to check each day price
        for val in prices:
            # If the previous day buy price is greater then today price, then
            # we will take today as new buy price
            if buy>=val:
                buy = val
            # As previous day buy price is less than today price then this is profit.
            # IF the profit is more than max profit, save this profit else continue with old max profit.
            else:
                temp=val-buy
                if temp>max_profit:
                    max_profit=temp
        return max_profit



s = Solution ()
prices = [7,6,4,3,1]
print (s.maxProfit(prices))