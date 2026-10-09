class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}

        for vex, nei in edges:
            graph[vex].append(nei)
            graph[nei].append(vex) 

        visited = set()

        # This one has to return int
        def dfs(vertex):
            if vertex in visited:
                return False
            if len(graph[vertex]) == 0:
                visited.add(vertex)
                return True

            visited.add(vertex)

            for nei in graph[vertex]:
                if nei in visited:
                    continue
                dfs(nei)
            return True

        count = 0
        for i in range(n):
            if dfs(i):
                count += 1
    
        return count