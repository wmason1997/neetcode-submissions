class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def isPalindrome(t):
            if t == t[::-1]:
                return True
            return False
        
        pCount = 0
        for i in range(0, len(s)):
            for j in range(i,(len(s))):
                if isPalindrome(s[i:j+1]):
                    pCount += 1
        
        return pCount
        