class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        before = None
        cur = head

        for i in range(left-1):
            before = cur
            cur = cur.next
        left_node = cur

        next = cur.next
        if next is not None:
            next_next = next.next
            for i in range(right-left):
                next.next = cur
                cur = next
                next = next_next
                if next is None:
                    break
                next_next = next_next.next

        left_node.next = next
        if before is not None:
            before.next = cur
        else:
            head = cur

        return head