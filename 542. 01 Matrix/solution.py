from typing import List
from collections import deque 


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        ans = [[-1 for _ in range(m)] for _ in range(n)]

        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= ni < n and 0 <= nj < m and ans[ni][nj] == -1:
                    ans[ni][nj] = ans[i][j] + 1
                    q.append((ni, nj))
                    
        return ans
