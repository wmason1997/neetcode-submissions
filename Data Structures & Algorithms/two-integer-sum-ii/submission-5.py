class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        trackingSet = {}
        difference = 0
        index1, index2 = 0, len(numbers) - 1

        while numbers[index1] + numbers[index2] != target:
    
            # if greater than target, move L right
            if numbers[index1] + numbers[index2] > target:
                index2 -= 1

            # if less than than target, move R right
            elif numbers[index1] + numbers[index2] < target:
                index1 += 1

        
        return [index1 + 1, index2 + 1]
        
            



            
