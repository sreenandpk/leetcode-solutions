# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        previous_node = None

        current_node = head


        while current_node is not None:

            # Save next node
            next_node = current_node.next

            # Reverse pointer
            current_node.next = previous_node

            # Move previous forward
            previous_node = current_node

            # Move current forward
            current_node = next_node


        return previous_node