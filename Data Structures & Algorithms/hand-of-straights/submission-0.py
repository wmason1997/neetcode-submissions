class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        

        while hand:
            start_of_straight = min(hand)
            for i in range(start_of_straight, start_of_straight + groupSize):
                if i not in hand:
                    return False
                else:
                    hand.remove(i)

        
        return True
