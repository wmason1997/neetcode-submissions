class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        T, B = 0, len(matrix)
        L, R = 0, len(matrix[0])

        res = []

        row, col = 0, 0

        while T < B and L < R:

            # go right
            for i in range(L, R):
                res.append(matrix[T][i])
            T += 1
            # go down
            for i in range(T, B):
                res.append(matrix[i][R-1])
            R -= 1
            if not (L < R and T < B):
                break
            # go left
            for i in range(R - 1, L - 1, -1):
                res.append(matrix[B -1][i])
            B -= 1

            # go up
            for i in range(B - 1, T - 1, -1):
                res.append(matrix[i][L])
            L += 1
        
        return res