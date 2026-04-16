class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for i in range(len(nums)):
            if nums[i] not in freqDict:
                freqDict[nums[i]] = 1
            elif nums[i] in freqDict:
                freqDict[nums[i]] += 1
    
        arr = []
        for num, cnt in freqDict.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res