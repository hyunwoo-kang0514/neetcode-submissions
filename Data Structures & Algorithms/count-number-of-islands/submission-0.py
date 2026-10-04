class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        row_len, col_len = len(grid), len(grid[0])
        island_num = 0
        visited = set()

        def bfs(row, col):
            direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            q = collections.deque()
            q.append((row, col))
            visited.add((row, col))
            while q:
                row, col = q.popleft()
                for (r,c) in direction:
                    new_row, new_col = row + r, col + c
                    if (new_row >= 0 and new_row < row_len and
                        new_col >= 0 and new_col < col_len and
                        grid[new_row][new_col] == "1" and
                        (new_row, new_col) not in visited):
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col))


        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    island_num += 1

        return island_num

    
        