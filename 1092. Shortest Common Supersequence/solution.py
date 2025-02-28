class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        old = [str2[i:] for i in range(m + 1)]

        for i in range(n - 1, -1, -1):
            new = [""] * (m + 1)
            new[-1] = str1[i:]

            for j in range(m - 1, -1, -1):
                if str1[i] == str2[j]:
                    new[j] = str1[i] + old[j + 1]
                elif len(new[j + 1]) <= len(old[j]):
                    new[j] = str2[j] + new[j + 1]
                else:
                    new[j] = str1[i] + old[j]

            old = new
                

        return old[0]        
