class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        while L < R:
            m = L + (R - L) // 2
            if nums[m] < nums[R]:
                R = m
            else:
                L = m + 1
        return nums[L]