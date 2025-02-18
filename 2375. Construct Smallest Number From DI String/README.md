# Intuition
First intuition was to use backtracking. But we can use a logic, while we encounter 'I' we can increment from smallest digit like 1, 2 ,3 if we encounter 'D' we can do the same thing but in reverse so for 3 D's will nedd 3, 2, 1. 

# Approach
Use a stack. Increment from smallest digit while encautering 'I' and pop from stack to maintain order. If encounter 'D' don't pop and store in stack until we find another 'I' or und of pattern in that case we pop from stack and receive reverse order. Ex. 4, 5, 6 -> 6, 5, 4 when popping.

# Complexity
- Time complexity:
$$O(n)$$ - iteration.

- Space complexity:
$$O(n)$$ - for stack.

# Code
```python3 []
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = ""
        
        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))
            
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    result += stack.pop()
        
        return result

```