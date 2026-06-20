class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dict = defaultdict(int)

        for i in range(n):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
            if dict[nums[i]] > n / 2.0:
                    return nums[i]