class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numDict = {}

        for i in range(len(nums)):
            if nums[i] not in numDict:
                numDict[nums[i]] = 1
            elif nums[i] in numDict:
                numDict[nums[i]] = 0
    
        for i in range(len(nums)):
            if numDict[nums[i]] == 1:
                return nums[i]