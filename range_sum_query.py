from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.row_sums = {}
        self.sums = {}
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == row2:
            return self.get_row_sum(row1, col1, col2)

        key = (row1, col1, row2, col2)
        if key in self.sums:
            return self.sums[key]

        sum = (self.get_row_sum(row1, col1, col2) 
            + self.sumRegion(row1+1, col1, row2, col2))

        self.sums[key] = sum
        return sum
    
    def get_row_sum(self, row, col1, col2):
        if row not in self.row_sums \
                or len(self.row_sums[row]) <= col2:
            self.setup_cumulative(row, col2)

        if col1 > 0:
            offset_sum = self.row_sums[row][col1-1]
        else:
            offset_sum = 0
        return self.row_sums[row][col2] - offset_sum

    def setup_cumulative(self, row, col2):
        matrix_row = self.matrix[row]
        if row in self.row_sums:
            cumulatives = self.row_sums[row]
        else:
            cumulatives = [matrix_row[0]]

        for i in range(len(cumulatives), col2+1):
            cumulatives.append(cumulatives[i-1] + matrix_row[i])
        
        self.row_sums[row] = cumulatives
