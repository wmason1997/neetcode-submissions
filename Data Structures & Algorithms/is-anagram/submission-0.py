class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstDict = {}
        secondDict = {}

        for i in range(len(s)):
            if s[i] in firstDict:
                firstDict[s[i]] += 1
            else:
                firstDict[s[i]] = 1

        for j in range(len(t)):
            if t[j] in secondDict:
                secondDict[t[j]] += 1
            else:
                secondDict[t[j]] = 1
        
        # firstDict = sorted(firstDict)
        # secondDict = sorted(secondDict)

        return firstDict == secondDict