class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        edges = set()
        visited = set()

        # process edge

        # up and down
        for i in range(COLS):
            if board[0][i] == "O":
                edges.add((0, i))
            if board[ROWS-1][i] == "O":
                edges.add((ROWS - 1, i))

        # left and right
        for i in range(ROWS):
            if board[i][0] == "O":
                edges.add((i, 0))
            if board[i][COLS - 1] == "O":
                edges.add((i, COLS-1))

        def isValidCell(newRow, newCol):
            if newRow < 0 or newRow >= ROWS:
                return False
            if newCol < 0 or newCol >= COLS: 
                return False
            if (newRow, newCol) in visited:
                return False
            if (newRow, newCol) in edges:
                return False
            if board[newRow][newCol] == "X":
                return False
            return True

        def bfs(i, j):
            visited.add((i, j))
            direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            q = deque()
            q.append((i, j))
            
            while q: 
                row, col = q.popleft()
                for l, r in direction:
                    newRow = row + l
                    newCol = col + r
                    if isValidCell(newRow, newCol):
                        visited.add((newRow, newCol))
                        edges.add((newRow, newCol))
                        q.append((newRow, newCol))

        for edge in list(edges):
            i, j = edge
            bfs(i, j)

        for i in range(ROWS):
            for j in range(COLS):
                if (
                    (i, j) not in edges 
                    and (i, j) not in visited
                    and board[i][j] == "O"
                ):
                    board[i][j] = "X"


        


                


        



                
        