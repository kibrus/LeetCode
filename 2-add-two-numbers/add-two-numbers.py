# from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to form the resulting linked list
        dummy = ListNode()
        current = dummy
        carry = 0  # To handle carries

        # Traverse both lists while there are nodes or a carry remains
        while l1 or l2 or carry:
            # Get the values from the current nodes (or 0 if a list is exhausted)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and update carry
            total = val1 + val2 + carry
            carry = total // 10  # Extract the carry
            new_val = total % 10  # Get the new digit
            
            # Create a new node with the computed value
            current.next = ListNode(new_val)
            current = current.next
            
            # Move to the next nodes in the input lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
