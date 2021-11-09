from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        if len(prices)<=1: return max_profit
        if prices[0]<=prices[1]:
            buy=prices[0]
            idx=1
        else:
            buy = prices[1]
            idx=2
        for val in prices[idx:]:
            if buy<val:
                max_profit+= (val-buy)
            buy=val
        return max_profit
s = Solution ()
prices = [7,6,4,3,1]
print (s.maxProfit(prices))