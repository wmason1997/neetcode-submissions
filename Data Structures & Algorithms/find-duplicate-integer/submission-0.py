class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seenSet = set()

        for i in range(len(nums)):
            if nums[i] in seenSet:
                return nums[i]
            seenSet.add(nums[i])