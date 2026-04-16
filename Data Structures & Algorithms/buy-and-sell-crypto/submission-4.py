class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1 # left=buy. right=sell
        maxP = 0

        while R < len(prices):
            #profitable ?
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                maxP = max(maxP, profit)
            else:
                L = R
            R += 1
        
        return maxP