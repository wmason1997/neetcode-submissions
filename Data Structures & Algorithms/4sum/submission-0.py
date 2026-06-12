from functools import lru_cache

class Solution:
    #@lru_cache
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    for l in range (k+1, len(nums)):
                        if (nums[i] + nums[j] + nums[k] + nums[l] == target): # and \
                        #     len(set([nums[i], nums[j], nums[k], nums[l]])) == 4):
                            # Check
                            sorted_array = [nums[i], nums[j], nums[k], nums[l]]
                            sorted_array.sort()
                            if sorted_array in res:
                                continue
                            res.append(sorted_array)
        
        return res