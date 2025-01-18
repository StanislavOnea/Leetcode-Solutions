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

