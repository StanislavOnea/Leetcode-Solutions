from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        indices = [(num, i) for i, num in enumerate(nums)]
        indices.sort()

        groups = []
        group = [indices[0]]
        for r in range(1, len(indices)):
            if indices[r][0] - group[-1][0] <= limit:
                group.append(indices[r])
            else:
                groups.append(group)
                group = [indices[r]]

        groups.append(group)
        for g in groups:
            sorted_idx = sorted(g, key=lambda x: x[1])
            for i, val in zip(sorted_idx, g):
                nums[i[1]] = val[0]


        return nums

