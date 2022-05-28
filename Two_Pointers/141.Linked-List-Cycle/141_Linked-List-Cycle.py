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
