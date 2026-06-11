from functools import lru_cache

class Solution:


    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def rec(i, bought):
            if i == len(prices):
                return 0
            res = rec(i + 1, bought)
            if bought: 
                return max(res, prices[i] + rec(i+1, False))
            else:
                return max(res, -prices[i] + rec(i+1, True))
        return rec(0, False)
