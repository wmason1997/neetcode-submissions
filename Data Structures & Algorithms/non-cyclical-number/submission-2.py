class Solution:
    def isHappy(self, n: int) -> bool:
        n_str = str(n)

        visited_set = []

        while True:
            loop_sum = 0
            for char in str(n):
                loop_sum += int(char) ** 2
            
            if n == 1:
                return True
            if n in visited_set:
                return False
            
            visited_set.append(n)
            n = loop_sum