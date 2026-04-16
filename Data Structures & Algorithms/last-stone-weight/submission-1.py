class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            a, b = stones.pop(), stones.pop()
            absolute = abs(a - b)
            if absolute > 0:
                stones.append(absolute)
    
        return stones[0] if stones else 0