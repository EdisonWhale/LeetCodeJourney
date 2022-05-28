# LeetCode Problem #141: Linked List Cycle

This repository contains a Python solution to LeetCode problem #141: Linked List Cycle. The function checks whether a given linked list has a cycle.

## Problem Statement

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. Note that `pos` is not passed as a parameter.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

### Constraints:

- Number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- `pos` is -1 or a valid index in the linked-list.

## Solution Approach

The solution employs Floyd's cycle-finding algorithm or the tortoise and the hare algorithm. This algorithm maintains two pointers, one slow (moving one step at a time) and one fast (moving two steps at a time). If a cycle exists in the list, the fast pointer eventually overlaps with the slow pointer.

## Code Explanation

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:  
            return False

        slow = head  # Slow pointer
        fast = head.next  # Fast pointer

        while slow != fast:  # Until pointers meet or end of list is reached
            if fast is None or fast.next is None:
                return False  # If end of list is reached, no cycle
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps

        return True

```