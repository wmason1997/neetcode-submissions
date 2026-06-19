class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        curLongest = ""
        shorterStringLength = min(len(str1), len(str2))
        for i in range(shorterStringLength):
            candidate = str1[:i+1]
            if str1 == candidate * (len(str1) // len(candidate)) and \
                str2 == candidate * (len(str2) // len(candidate)):
                curLongest = candidate
            else:
                continue
        return curLongest