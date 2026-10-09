class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graphMap = {i : [] for i in range(n)}
        # Create undirected graph
        for v, nei in edges:
            graphMap[v].append(nei)
            graphMap[nei].append(v)

        visited = set()
        
        # Parent가 아닌데 만약에 visited에 있는 요소가 한 번 더 나올경우 cycle

        def dfs(p, v):
            if v in visited:
                return False

            visited.add(v)

            for n in graphMap[v]:
                if n == p:
                    continue
                if not dfs(v, n):
                    return False
            return True

        if not dfs(-1, 0):
            return False
            
        return len(visited) == n
                
            




                