class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()
        cycle = set()

        courseSchedule = []

        def dfs(crs):
            # 현재 DFS 경로에서 다시 만남 = cycle
            if crs in cycle:
                return False
            # 이미 처리 끝난 course
            if crs in visit:
                return True
            cycle.add(crs)

            # prerequisite 먼저 방문
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # 현재 DFS 경로에서 제거
            cycle.remove(crs)

            # 이제 이 course는 완전히 처리됨
            visit.add(crs)

            # prerequisite가 모두 먼저 들어갔으므로
            # 이제 현재 course를 넣음
            courseSchedule.append(crs)

            return True

        for crs in preMap.keys():
            if not dfs(crs):
                return []

        return courseSchedule