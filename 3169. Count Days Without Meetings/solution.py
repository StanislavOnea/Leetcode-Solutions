from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        merged = []

        for s, e in meetings:
            if not merged:
                merged.append([s, e])
                continue
            
            if merged[-1][1] >= s:
                last = merged.pop()
                merged.append([last[0], max(e, last[1])])
            else:
                merged.append([s, e])

        working_days = 0
        for s, e in merged:
            working_days += e - s + 1

        return days - working_days
