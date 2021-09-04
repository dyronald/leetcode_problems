import unittest
from compare_version import Solution, VersionWalker


class TestSolution(unittest.TestCase):
    def test_method_exists(self):
        s = Solution()
        s.compareVersion('1.0', '1.0')

    def test_equal_rev(self):
        s = Solution()
        result = s.compareVersion('1.0', '1.0')
        self.assertEqual(0, result)

    def test_lower_rev1(self):
        s = Solution()
        result = s.compareVersion('1.1', '2.0')
        self.assertEqual(-1, result)

    def test_greater_rev1(self):
        s = Solution()
        result = s.compareVersion('3.0', '2.1')
        self.assertEqual(1, result)

    def test_lower_rev2(self):
        s = Solution()
        result = s.compareVersion('2.1', '2.2')
        self.assertEqual(-1, result)

    def test_greater_rev2(self):
        s = Solution()
        result = s.compareVersion('3.3', '3.2')
        self.assertEqual(1, result)

    def test_greater_rev2_equal_rev3(self):
        s = Solution()
        result = s.compareVersion('3.3.3', '3.2.3')
        self.assertEqual(1, result)

    def test_unequal_version_length(self):
        s = Solution()
        result = s.compareVersion('3.10', '3.10.1')
        self.assertEqual(-1, result)


class TestVersionWalker(unittest.TestCase):
    def test_create(self):
        rw = VersionWalker('1.0')

    def test_get_first_revision(self):
        vw = VersionWalker('1.0')
        first = vw.next()
        self.assertEqual(1, first)

    def test_get_revision2(self):
        vw = VersionWalker('1.23.1')
        vw.next()
        rev2 = vw.next()
        self.assertEqual(23, rev2)

    def test_get_last_revision(self):
        vw = VersionWalker('1.23.34')
        vw.next()
        vw.next()
        last = vw.next()
        self.assertEqual(34, last)

    def test_return_none_after_last(self):
        vw = VersionWalker('1.23.34')
        vw.next()
        vw.next()
        vw.next()
        after_last = vw.next()
        self.assertEqual(after_last, None)
