class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visited = set()
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        maxArea = 0

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
            q.append((i, j))
            area = 1
            
            while q:
                row, col = q.popleft()
                for x, y in direction:
                    newRow = row + x
                    newCol = col + y
                    if isPartOfIsland(newRow, newCol):
                        visited.add((newRow, newCol))
                        q.append((newRow, newCol))
                        area += 1

            return area
                    
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited and grid[i][j] == 1:
                    area = bfs(i, j)
                    maxArea = max(area, maxArea)

        return maxArea
        