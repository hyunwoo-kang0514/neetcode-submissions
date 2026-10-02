class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # declaring hash map
        hash_map = {}
        arr = []
        for point in points:
            distance = point[1] ** 2 + point[0] ** 2
            if distance not in hash_map:
                hash_map[distance] = []  # value는 아무거나 가능하다.
            hash_map[distance].append(point)
            arr.append(distance)

        arr.sort()
        res = []

        for i in range(k):
            res.append(hash_map[arr[i]].pop())
        return res


