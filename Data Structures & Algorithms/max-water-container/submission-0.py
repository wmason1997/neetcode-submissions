class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # L, R = 0, len(heights) - 1
        # maxL, maxR = L, R
        maxWater = 0

        for L in range(len(heights) - 1):
            R = L + 1
            while R < len(heights) and L < R:
                waterVolume = (R - L) * min(heights[L], heights[R])
                maxWater = max(maxWater, waterVolume)
                R += 1
        
        return maxWater


        