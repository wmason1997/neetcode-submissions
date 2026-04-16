class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxSetLength = 0

        for i in range(len(nums)):
            # Check if left neighbor (n - 1)
            thisSetLength = 1
            priorValue = nums[i] - 1
            while priorValue in numsSet:
                # if so, keep going until no more
                # update maxSetLength
                priorValue = priorValue - 1
                thisSetLength += 1

            maxSetLength = max(maxSetLength, thisSetLength)
        
        return maxSetLength