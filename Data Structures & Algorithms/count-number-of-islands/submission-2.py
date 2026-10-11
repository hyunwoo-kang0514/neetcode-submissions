class Solution:
    # Second try
    # Using bfs
    # First step
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        numIsland = 0


        def isPartOfIsland(newRow, newCol):
            if newRow < 0 or newRow >= ROWS:
                return False
            if newCol < 0 or newCol >= COLS:
                return False
            if grid[newRow][newCol] == 0:
                return False
            if (newRow, newCol) in visited:
                return False
            return True
               


        def bfs(i, j):
            visited.add((i, j))
            queue = deque()
            queue.append((i, j))
            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                row, col = queue.popleft()
                for x, y in direction:
                    newRow = row + x
                    newCol = col + y
                    if isPartOfIsland(newRow, newCol):
                        visited.add((newRow, newCol))
                        queue.append((newRow, newCol))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "0":
                    grid[i][j] = 0
                else:
                    grid[i][j] = 1


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    bfs(i, j)
                    numIsland += 1

        return numIsland
