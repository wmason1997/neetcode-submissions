class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        
        N = len(triplets)
        A, B, C = target
        if N == 1:
            return triplets[0] == target

        for i in range(N - 1):
            for j in range(i + 1, N):
                if target == [max(triplets[i][0], triplets[j][0]), 
                              max(triplets[i][1], triplets[j][1]),
                              max(triplets[i][2], triplets[j][2])]:                    
                    return True
                elif (max(triplets[i][0], triplets[j][0]) <= A and
                     max(triplets[i][1], triplets[j][1]) <= B and
                     max(triplets[i][2], triplets[j][2]) <= C):
                    triplets[j] = [max(triplets[i][0], triplets[j][0]), 
                                   max(triplets[i][1], triplets[j][1]),
                                   max(triplets[i][2], triplets[j][2])]
                else:
                    continue
        return False