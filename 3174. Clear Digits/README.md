# Intuition
Using a stack for poping chars before digits.
# Approach
Append to stack chars until we find a digit. If we find a digit don't append but pop the last element. At the end display the content of stack. 
# Complexity
- Time complexity:
O(n) - for iteration.

- Space complexity:
O(n) - space for stack.

# Code
```python3 []
class Solution:
    def clearDigits(self, s: str) -> str:
        st = []

        for ch in s:
            if ch.isdigit():
                st.pop()
            else:
                st.append(ch)
        
        return "".join(st)

```