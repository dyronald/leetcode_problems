import unittest
from unittest.mock import Mock
from range_sum_query import NumMatrix#, RowSums


class Test(unittest.TestCase):
    def test_method_exists(self):
        n = NumMatrix([[1,2], [3,4]])
        n.sumRegion(0, 0, 1, 1)

    def test_get_sum_subset_rectangle(self):
        n = NumMatrix([[1,2,3,4], [5,6,7,8,], [1,2,3,4]])
        result = n.sumRegion(0, 0, 1, 1)
        self.assertEqual(14, result)

    def test_get_sum_single_cell(self):
        n = NumMatrix([[1,2,3,4], [5,6,7,8,], [1,2,3,4]])
        result = n.sumRegion(0, 0, 0, 0)
        self.assertEqual(1, result)


# class RowCumulativeSumsTest(unittest.TestCase):
#     def test_can_instantiate(self):
#         obj = RowSums([[1,2,3,4], [5,6,7,8], [1,2,3,4]])

#     def test_get_row_sum(self):
#         obj = RowSums([[1,2,3,4], [5,6,7,8], [1,2,3,4]])
#         result = obj.sum(1, 2, 3)
#         self.assertEqual(15, result)

#     def test_get_row_repeated_row_query(self):
#         obj = RowSums([[1,2,3,4], [5,6,7,8], [1,2,3,4]])
#         mock = Mock(wraps=obj.setup_cumulative)
#         obj.setup_cumulative = mock
#         obj.sum(1, 2, 3)
#         obj.sum(1, 0, 1)
#         obj.sum(1, 1, 2)

#         self.assertEqual(1, mock.call_count)

#     def test_single_cell_sum(self):
#         obj = RowSums([[1,2,3,4], [5,6,7,8], [1,2,3,4]])
#         result = obj.sum(1, 2, 2)
#         self.assertEqual(7, result)

#     def test_first_cell_sum(self):
#         obj = RowSums([[1,2,3,4], [5,6,7,8], [1,2,3,4]])
#         result = obj.sum(1, 0, 0)
#         self.assertEqual(5, result)

#     def test_last_cell_sum(self):
#         obj = RowSums([[1,2,3,4], [5,6,7,8], [1,2,3,4]])
#         result = obj.sum(1, 3, 3)
#         self.assertEqual(8, result)
