import unittest
from swap_nodes_in_pairs import Solution, ListNode

def _input(*node_vals):
    if len(node_vals) == 0:
        return None

    head = ListNode(node_vals[0])
    current = head
    for v in node_vals[1:]:
        current.next = ListNode(v)
        current = current.next
    return head

def _get_vals(node_list):
    vals = []
    current = node_list
    while current is not None:
        vals.append(current.val)
        current = current.next
    return vals

class Test(unittest.TestCase):
    def test_simple_input(self):
        result = Solution().swapPairs(_input(1,2,3,4))
        self.assertEqual([2,1,4,3], _get_vals(result))

    def test_empty(self):
        result = Solution().swapPairs(None)
        self.assertEqual([], _get_vals(result))

    def test_single_input(self):
        result = Solution().swapPairs(_input(1))
        self.assertEqual([1], _get_vals(result))

    def test_odd_list_size(self):
        result = Solution().swapPairs(_input(1,2,3,4,5))
        self.assertEqual([2,1,4,3,5], _get_vals(result))

    def test_list_size_3(self):
        result = Solution().swapPairs(_input(1,2,3))
        self.assertEqual([2,1,3], _get_vals(result))

    def test_list_size_2(self):
        result = Solution().swapPairs(_input(1,2))
        self.assertEqual([2,1], _get_vals(result))
