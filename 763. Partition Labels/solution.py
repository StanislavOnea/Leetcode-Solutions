from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {c: i for i, c in enumerate(s)}
        res = []

        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end, last_index[s[i]])

            if end == i:
                res.append(end - start + 1)
                start = end + 1

        return res
    