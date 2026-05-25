class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n > 0:
            temp = 1.0
            for _ in range(n):
                temp *= x
            return temp
        elif n < 0:
            temp = 1.0
            for _ in range(-n):
                temp *= x
            return 1.0 / temp