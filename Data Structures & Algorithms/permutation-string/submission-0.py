class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        sorted_s1 = sorted(s1)

        if s2_len < s1_len:
            return False
        
        if s1_len == 0:
            return True
    
        for i in range(s2_len - s1_len+1):
            # for j in range(i + 1, s2_len - s1_len + 1):
            if sorted(s2[i:i+s1_len]) == sorted_s1:
                return True
        
        return False