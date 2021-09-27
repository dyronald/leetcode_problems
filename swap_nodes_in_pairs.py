from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head

        swapped_head = head.next

        prev_node = self.swapPair(None, head)
        while prev_node is not None:
            curr_node = prev_node.next
            prev_node = self.swapPair(prev_node, curr_node)

        return swapped_head

    def swapPair(self, prev_node, node1):
        if node1 is not None:
            node2 = node1.next
            if node2 is None:
                return None

            if prev_node is not None:
                prev_node.next = node2
            node1.next = node2.next
            node2.next = node1

        return node1
