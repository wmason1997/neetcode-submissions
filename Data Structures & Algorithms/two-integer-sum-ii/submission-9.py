class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L < R:
            # if sum is too small, plus one to left
            if numbers[L] + numbers[R] < target:
                L += 1

            # if sum is too large, minus one to right
            elif numbers[L] + numbers[R] > target:
                R -= 1

            # else:
            else:
                return [L + 1, R + 1]

        # Correct for 1 index
        #return [L + 1, R + 1]