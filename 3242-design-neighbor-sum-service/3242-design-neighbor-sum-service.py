class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.pos = {}
        for i in range(len(grid)):
            for j in range(len(grid)):
                self.pos[grid[i][j]] = (i, j)

    def adjacentSum(self, value: int) -> int:
        i, j = self.pos[value]
        n = len(self.grid)
        return sum(self.grid[a][b] for a, b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] if 0 <= a < n and 0 <= b < n)

    def diagonalSum(self, value: int) -> int:
        i, j = self.pos[value]
        n = len(self.grid)
        return sum(self.grid[a][b] for a, b in [(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)] if 0 <= a < n and 0 <= b < n)
