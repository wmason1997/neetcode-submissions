class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        L, R = 0, len(nums) - 1
        while L <= R:
            M = L + (R - L) // 2
            if nums[M] == target:
                return True
            
            if nums[L] < nums[M]: # Left portion

                if nums[L] <= target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1
            elif nums[L] > nums[M]: # Right portion
                if nums[M] < target <= nums[R]:
                    L = M + 1
                else:
                    R = M - 1
            else:
                L += 1
        
        return False