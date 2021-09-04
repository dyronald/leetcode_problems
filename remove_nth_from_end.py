import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        win_size = n+1
        window, list_cur = self.init_window(head, win_size)
        if len(window) < win_size:
            return head.next

        while list_cur is not None:
            window.append(list_cur)
            list_cur = list_cur.next

        before = window[0]
        before.next = before.next.next

        return head

    def init_window(self, head, win_size):
        window = collections.deque([], maxlen=win_size)
        cur = head
        while len(window) < win_size and cur is not None:
            window.append(cur)
            cur = cur.next

        return window, cur

        