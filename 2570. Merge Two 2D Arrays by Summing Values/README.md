# Intuition
Use 2 pointer aproach and act similar as merging 2 sorted list just keep in mind the additional condition of the problem.

# Approach
Iterate over both list at each step check if nums1[i] == nums2[j] then proceed with problem logic of adding values and append to res. If nums1[i] is less (idnex) than nums2[j] add nums2[j] to result list.

# Complexity
- Time complexity:
$$O(n)$$ - for traversal.

- Space complexity:
$$O(1)$$ - pointers (if don't consider output as space complexity).

# Code
```python3 []
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []

        while i < len(nums1) and j < len(nums2):
            num1 = nums1[i]
            num2 = nums2[j]

            if num1[0] == num2[0]:
                res.append([num1[0], num1[1] + num2[1]])
                i += 1
                j += 1
            elif num1[0] <= num2[0]:
                res.append(num1)
                i += 1
            else:
                res.append(num2)
                j += 1

        for idx in range(i, len(nums1)):
            res.append(nums1[idx])

        for idx in range(j, len(nums2)):
            res.append(nums2[idx])

        return res

```