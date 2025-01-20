# Intuition
We can calculate it like we do on a paper but starting adding from the left to right.

# Approach
If the sum of 2 nodes exceeds 9 then we write the remainin value % 10 and we will add it to the next sum. The only case when we need to adjust the list lenght is when we still have an aditional 1 to add but there is no more nodes - in that case we create a new node and atach it the the last node os our answer.

# Complexity
- Time complexity:
O(n) - we iterate through the both lists.
O(max(l1, l2))

Since we have to go trough all of the cells (N * M) but also add in the worst case all cells from grid to the min-heap log(N * M).

- Space complexity:
We keep only our answer in memory so technically it's O(1)

# Code
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2

        addition = 0
        ans = ListNode()
        tmp = ans
        while curr1 or curr2:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            value = val1 + val2 + addition
            addition = 0
            if value >= 10:
                value = value % 10
                addition = 1
            tmp.next = ListNode(val=value)

            tmp = tmp.next
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        
        if addition:
            tmp.next = ListNode(val=addition)
        return ans.next

```