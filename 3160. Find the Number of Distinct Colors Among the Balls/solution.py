from typing import List
from collections import Counter


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = Counter()
        res = []

        for x, y in queries:
            prev_color = balls.get(x, 0)
            if prev_color:
                colors[prev_color] -= 1
                if colors[prev_color] == 0:
                    colors.pop(prev_color)

            colors[y] += 1
            balls[x] = y
            res.append(len(colors))

        return res
