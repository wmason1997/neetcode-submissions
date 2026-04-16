class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L, R = 0, len(prices) - 1
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                L = i
                R = j
                if prices[L] < prices[R]:
                    calc = prices[R] - prices[L]
                    res = max(res, calc)
        return res
            