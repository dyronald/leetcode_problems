from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for start_x in range(9):
            if not self._is_valid_region(board, start_x, 0, start_x + 1, 9):
                return False
        for start_y in range(9):
            if not self._is_valid_region(board, 0, start_y, 9, start_y + 1):
                return False

        for start_x in range(0, 9, 3):
            for start_y in range(0, 9, 3):
                if not self._is_valid_region(
                    board, start_x, start_y, start_x + 3, start_y + 3
                ):
                    return False

        return True

    def _is_valid_region(self, board, start_x, start_y, end_x, end_y):
        found = set()
        for x in range(start_x, end_x):
            for y in range(start_y, end_y):
                val = board[y][x]
                if val in found and val != ".":
                    return False
                else:
                    found.add(val)

        return True


[
    [".", ".", ".", ".", ".", ".", "5", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["9", "3", ".", ".", "2", ".", "4", ".", "."],
    [".", ".", "7", ".", ".", ".", "3", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "3", "4", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "."],
    [".", ".", ".", ".", ".", "5", "2", ".", "."],
]
