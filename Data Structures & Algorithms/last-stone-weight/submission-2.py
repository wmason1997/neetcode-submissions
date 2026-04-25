class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Sort stone

        while len(stones) >= 2:
            # sort stones
            stones.sort()
            stone1 = stones.pop()
            stone2 = stones.pop()

            if abs(stone1 - stone2) > 0:
                stones.append(abs(stone1 - stone2))
        
        return stones[0] if stones else 0