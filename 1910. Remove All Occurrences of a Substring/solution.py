class Solution1:
    def removeOccurrences(self, s: str, part: str) -> str:
        part_len = len(part)
        j = 0

        curr = ""
        for i in range(len(s)):
            
            curr += s[i]
            j += 1

            if j - part_len >= 0 and curr[j - part_len:] == part:
                curr = curr[:j - part_len]
                j = j - part_len

        if curr == part:
            return ""
        return curr


class Solution2:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "",1)
        return s
