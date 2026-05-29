class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Step 1: record last index of each character
        last = {char: i for i, char in enumerate(s)}

        result = []
        partition_start = 0
        partition_end = 0

        for i, char in enumerate(s):
            # Expand partition end to the furthest last occurrence seen so far
            partition_end = max(partition_end, last[char])

            # If we've reached the end of this partition, cut here
            if i == partition_end:
                result.append(partition_end - partition_start + 1)
                partition_start = i + 1

        return result