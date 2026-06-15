class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        
        lens = []
        for s in strs:
            lens.append(len(s))
        max_possible_prefix_length = min(lens)

        for i in range(max_possible_prefix_length):
            # check if all ith characters across strings are same
            # if not return common_prefix
            # if yes, grow common_prefix
            char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] == char:
                    continue
                else:
                    return common_prefix
            common_prefix += char
        
        return common_prefix
        
        