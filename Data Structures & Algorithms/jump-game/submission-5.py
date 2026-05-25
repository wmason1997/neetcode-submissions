class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = ['TBD'] * len(nums)
        def dfs(i):
            if i >= len(nums) - 1:
                return True
            if memo[i] != 'TBD':
                return memo[i]
            
            for j in range(nums[i], 0, -1):
                if dfs(i + j):
                    memo[i] = True
                    return True
            
            memo[i] = False
            return False

        return dfs(0)