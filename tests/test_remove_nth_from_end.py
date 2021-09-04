import unittest
from remove_nth_from_end import Solution, ListNode

class TestRemoveFromEnd(unittest.TestCase):
    def test_remove_middle_node(self):
        s = Solution()
        nodes = self.build_nodes([1, 2, 3, 4, 5])
        result = s.removeNthFromEnd(nodes, 3)
        self.check_nodes(result, [1,2,4,5])

    def test_remove_last_node_in_list(self):
        s = Solution()
        nodes = self.build_nodes([1])
        result = s.removeNthFromEnd(nodes, 1)
        self.check_nodes(result, [])

    def test_remove_last_node_one_node_remaining(self):
        s = Solution()
        nodes = self.build_nodes([1, 2])
        result = s.removeNthFromEnd(nodes, 1)
        self.check_nodes(result, [1])

    def test_remove_head_node(self):
        s = Solution()
        nodes = self.build_nodes([1, 2])
        result = s.removeNthFromEnd(nodes, 2)
        self.check_nodes(result, [2])

    def test_remove_from_big_list(self):
        s = Solution()
        nodes = self.build_nodes(range(100))
        result = s.removeNthFromEnd(nodes, 2)
        self.check_nodes(result, [*range(98), 99])

    def build_nodes(self, nodes_list):
        head = ListNode(nodes_list[0])
        cur = head

        for n in nodes_list[1:]:
            cur.next = ListNode(n)
            cur = cur.next
        
        return head

    def check_nodes(self, result, expected):
        cur = result

        for e in expected:
            self.assertEqual(cur.val, e)
            cur = cur.next
        
        self.assertIsNone(cur)
