# Intuition
Use backtracking, when adding a digit add automatically the next position where that digit's twin should be if digit > 1.
# Approach
Keep a counter fir tracking used digits from range 1..n. When inserting output sequence a digit check if its not 1 and if it is then add to position i + digit the digit twin and check if there are already an element if so then the sequence is not correct so return. If sequence[i] cotains a value then we should continue to next cell. If the algo iterate trough the len of sequence that means the constraints are met so we can return our sequence. Chose firstly the largest digits so it will guarantee that we will achive the Lexicographically Largest Valid Sequence first.

# Complexity
- Time complexity:
$$O(2^n)$$ - due tu backtracking.

- Space complexity:
$$O(n)$$ - result sequence and counter.

# Code
```python3 []
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
```