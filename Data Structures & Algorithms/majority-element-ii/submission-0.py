class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threshold = n // 3

        count = defaultdict(int)

        # build dict
        for num in nums:
            count[num] += 1
        
        return_array = []
        # extract values from dict
        for key, value in count.items():
            if value > threshold:
                return_array.append(key)
        
        return return_array
        