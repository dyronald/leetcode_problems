class Solution:
    memo = {}

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1

        key = (m, n)
        if key in self.memo:
            return memo[key]

        down = 0
        right = 0
        if m > 1:
            down = self.uniquePaths(m-1, n)
        if n > 1:
            right = self.uniquePaths(m, n-1)
        paths = right+down

        self.memo[key] = paths
        return paths