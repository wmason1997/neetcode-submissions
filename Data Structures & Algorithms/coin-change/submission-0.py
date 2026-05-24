class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Want the coins to be in ascending order
        # In order to minimize total coins to create amount
        # we want to maximize use of highest coin value
        # (until it creates a remaining sum that is impossible to create with remaining coins)

        # Want to track possible configurations that multiply to amount
        # Return min(sum) of those

        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            
            memo[amount] = res
            return res
        
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins


        