class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()

        def addFruit(row, col):
            if row < 0 or row >= ROWS:
                return 
            if col < 0 or col >= COLS:
                return
            if grid[row][col] != 1:
                return
            q.append((row, col))
            grid[row][col] = 2

            
        def bfs():
            time = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    addFruit(r + 1, c)
                    addFruit(r - 1, c)
                    addFruit(r, c + 1)
                    addFruit(r, c - 1)
                time += 1

            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == 1:
                        return -1
            return max(0, time - 1)


        # Iterate grid to append cell of rotten fruits
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))

        return bfs()




        # Lastly check if there is a remaining fresh fruit
        