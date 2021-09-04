from typing import List
from dataclasses import dataclass

@dataclass
class Coord:
    x: int
    y: int

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        layers = n // 2

        for l in range(layers):
            self.rot_layer(matrix, n, l)

        return matrix
        
    def rot_layer(self, matrix, n, layer):
        for index in range(n-(layer*2)-1):
            top_val = self.read(matrix, self.top(n, layer, index))
            self.assign(
                matrix,
                self.top(n, layer, index), 
                self.read(matrix, self.left(n, layer, index)))
            self.assign(
                matrix,
                self.left(n, layer, index), 
                self.read(matrix, self.bottom(n, layer, index)))
            self.assign(
                matrix,
                self.bottom(n, layer, index), 
                self.read(matrix, self.right(n, layer, index)))
            self.assign(
                matrix,
                self.right(n, layer, index), 
                top_val)
    
    def top(self, n, layer, index):
        return Coord(index+layer, 0+layer)
    
    def right(self, n, layer, index):
        return Coord(n-1-layer, index+layer)
    
    def bottom(self, n, layer, index):
        return Coord(n-1-layer-index, n-1-layer)

    def left(self, n, layer, index):
        return Coord(layer, n-1-layer-index)

    def read(self, matrix, coord):
        return matrix[coord.y][coord.x]

    def assign(self, matrix, dest, value):
        matrix[dest.y][dest.x] = value

