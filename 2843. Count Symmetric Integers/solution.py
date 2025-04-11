from typing import List


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for d in range(1, 10):
            num = d * 10 + d
            if low <= num <= high:
                count += 1

        prefix_by_sum = [[] for _ in range(19)]
        suffix_by_sum = [[] for _ in range(19)]

        for a in range(1, 10):
            for b in range(10):
                total = a + b
                prefix_by_sum[total].append(1000 * a + 100 * b)

        for c in range(10):
            for d in range(10):
                total = c + d
                suffix_by_sum[total].append(10 * c + d)

        for digit_sum in range(19):
            for prefix in prefix_by_sum[digit_sum]:
                for suffix in suffix_by_sum[digit_sum]:
                    num = prefix + suffix
                    if low <= num <= high:
                        count += 1

        return count
