import heapq
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

def find_largest_less_than(arr, x):
    left, right = 0, len(arr) - 1
    best_index = -1  # Default to -1 if no valid index is found

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < x:
            best_index = mid  # Update best candidate
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return best_index
print(find_largest_less_than([1,2,3,6,6,7,8,9, 10], 6))