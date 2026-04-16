class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # loop over the staring indices
            # if able to reach start, return i
        
        # if none worked, return -1

        # for loop across all possible starting gas station positions
        for i in range(len(gas)):
            tank = 0
            starting_i = i
            while tank + gas[i] - cost[i] >= 0:
                tank = tank + gas[i] - cost[i]
                i = (i + 1) % len(gas)
                if i == starting_i:
                    return i
                
        
        return -1