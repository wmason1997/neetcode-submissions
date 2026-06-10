class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        cur, store = 0, set(nums)
        for num in nums:
            cur = 0
            while num in store:
                cur +=1
                num += 1
                res = max(res, cur)
        return res