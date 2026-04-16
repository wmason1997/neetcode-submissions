class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        ithDayMap = {}

        for i in range(len(prices) - 1):
            start = prices[i]
            end = max(prices[i+1:])
            ithDayMap[i] = max(end - start, 0)
        
        # return max(ithDayMap.values())
        return max(list(ithDayMap.values()))