class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N + 1)]
        size = [1] * (N + 1)

        # find parent of x
        def find(n):
            if n == par[n]:
                return par[n]
            par[n] = find(par[n])
            return par[n]

        # union two verticies
        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return False
            
            if size[p1] > size[p2]:
                par[p2] = p1
                size[p1] += size[p2]
            else:
                par[p1] = p2
                size[p2] += size[p1]
            return True

        for x, y in edges:
            if not union(x, y):
                return [x, y]
        

        


                




        

        