class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        row_len = len(grid)
        col_len = len(grid[0])
        max_area = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            visited.add((r,c))
            size = 1

            while q:
                row, col = q.popleft()
                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]
                    if (
                        new_row in range(row_len) and
                        new_col in range(col_len) and 
                        grid[new_row][new_col] == 1 and
                        (new_row, new_col) not in visited
                    ):
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))
                        size += 1
            return size


        for i in range(row_len):
            for j in range(col_len):
                if (i, j) not in visited and grid[i][j] == 1:
                    max_area = max(bfs(i, j), max_area)

        return max_area
                    
                

        