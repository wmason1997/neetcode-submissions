class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMax = 0

        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                curMax = max(curMax, prices[j] - prices[i])
        
        return curMax
