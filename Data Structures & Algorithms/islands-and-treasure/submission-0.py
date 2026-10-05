class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])

        visited = set()
        q = deque()

        def addRoom(r, c):
            if (
                r < 0 or r >= ROW or
                c < 0 or c >= COL or
                (r, c) in visited or
                grid[r][c] == -1
            ):
                return

            visited.add((r, c))
            q.append((r, c))

        # 모든 treasure를 시작점으로 넣기
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))   # 이게 빠졌음

        dist = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist

                addRoom(r, c + 1)
                addRoom(r, c - 1)
                addRoom(r + 1, c)
                addRoom(r - 1, c)

            dist += 1