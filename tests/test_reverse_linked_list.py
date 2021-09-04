import unittest
from reverse_linked_list import Solution, ListNode

class Test(unittest.TestCase):

    def test_make_list(self):
        l = self.make_list([1,2,3,4,5])
        self.verify_list(l, [1,2,3,4,5])

    def test_reverse_middle(self):
        s = Solution()
        nodes = self.make_list([1,2,3,4,5])
        result = s.reverseBetween(nodes, 2, 4)
        self.verify_list(result, [1,4,3,2,5])

    def test_reverse_left(self):
        s = Solution()
        nodes = self.make_list([1,2,3,4,5])
        result = s.reverseBetween(nodes, 1, 3)
        self.verify_list(result, [3,2,1,4,5])

    def test_reverse_right(self):
        s = Solution()
        nodes = self.make_list([1,2,3,4,5])
        result = s.reverseBetween(nodes, 3, 5)
        self.verify_list(result, [1,2,5,4,3])

    def test_reverse_single_right(self):
        s = Solution()
        nodes = self.make_list([1,2,3,4,5])
        result = s.reverseBetween(nodes, 5, 5)
        self.verify_list(result, [1,2,3,4,5])

    def test_reverse_single_left(self):
        s = Solution()
        nodes = self.make_list([1,2,3,4,5])
        result = s.reverseBetween(nodes, 1, 1)
        self.verify_list(result, [1,2,3,4,5])

    def make_list(self, nodes):
        head = ListNode(val=1)
        cur = head
        for i in nodes[1:]:
            cur.next = ListNode(val=i)
            cur = cur.next
        return head

    def verify_list(self, result, expected):
        r_list = []
        c = result
        while c is not None:
            r_list.append(c.val)
            c = c.next

        self.assertEqual(r_list, expected)
