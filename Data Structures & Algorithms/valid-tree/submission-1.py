class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = {i: [] for i in range(n)}

        for v, nei in edges:
            edgeMap[v].append(nei)
            edgeMap[nei].append(v)

        visited = set()

        def dfs(v, parent):
            if v in visited:
                return False

            visited.add(v)

            for nei in edgeMap[v]:
                if nei == parent:
                    continue

                if not dfs(nei, v):
                    return False
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n