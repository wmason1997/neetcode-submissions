class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        # Check if that set is in the dictionary yet
        for string in strs:
            sortedstring = ''.join(sorted(string))
            res[sortedstring].append(string)
        return list(res.values())

