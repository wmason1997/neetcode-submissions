class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        # maxL, maxR = L, R
        maxWater = 0

        while L < R:
            waterVolume = (R - L) * min(heights[L], heights[R])
            maxWater = max(maxWater, waterVolume)
            #R += 1

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        
        return maxWater