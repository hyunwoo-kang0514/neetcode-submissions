class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit, cycle = set(), set()
        courseSchedule = []

        def dfs(crs):  
            if crs in visit:
                return True
            if crs in cycle: 
                return False

            cycle.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            courseSchedule.append(crs)
            return True
        
        for course in preMap:
            if not dfs(course):
                return []

        return courseSchedule