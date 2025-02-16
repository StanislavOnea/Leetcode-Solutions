from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        len_seq = (n * 2 -1)
        sequence = [0] * len_seq
        counter = [0] * (n + 1)

        for i in range(1, n + 1):
            counter[i] += 1
        def backtracking(i):
            if i >= len_seq:
                return sequence[:]
            if sequence[i]:
                return backtracking(i + 1)
            
            result = []
            for j in range(n, 0, -1):
                if counter[j] <= 0:
                    continue
                counter[j] -= 1
                if j > 1:
                    if i + j < len_seq and not sequence[i + j]:
                        sequence[i] = j
                        sequence[i + j] = j
                    else:
                        counter[j] += 1
                        continue

                    result = backtracking(i + 1)

                    if result:
                        return result

                    sequence[i] = 0
                    sequence[i + j] = 0
                else:
                    sequence[i] = j
                    result = backtracking(i + 1)

                    if result:
                        return result

                    sequence[i] = 0
                counter[j] += 1

            return []

        return backtracking(0)
