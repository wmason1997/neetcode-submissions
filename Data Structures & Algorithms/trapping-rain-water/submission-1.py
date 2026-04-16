class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        L, R = 0, len(height) - 1
        leftMax, rightMax = height[L], height[R]
        res = 0

        # Only need to check when L and R are at least 2 apart

        while L < R:
            if leftMax < rightMax:
                L += 1
                leftMax = max(leftMax, height[L])
                res += leftMax - height[L] #if leftMax - height[L] > 0 else 0
            else:
                R -= 1
                rightMax = max(rightMax, height[R])
                res += rightMax - height[R] #if rightMax - height[R] > 0 else 0
            
        return res