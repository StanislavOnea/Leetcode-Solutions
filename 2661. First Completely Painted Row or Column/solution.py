from typing import List
from collections import defaultdict


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        coordinates = {}

        for i in range(n):
            for j in range(m):
                coordinates[mat[i][j]] = (i, j)

        rows = defaultdict(int)
        cols = defaultdict(int)
        for i in range(len(arr)):
            mat_i, mat_j = coordinates[arr[i]]
            rows[mat_i] += 1
            cols[mat_j] += 1
            if rows[mat_i] == m or cols[mat_j] == n:
                return i

        return -1
    
