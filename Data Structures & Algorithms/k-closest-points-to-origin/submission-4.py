class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hash_map = {}
        arr = []

        for li in points:
            distance = li[0] ** 2 + li[1] ** 2

            if distance not in hash_map:
                hash_map[distance] = []

            hash_map[distance].append(li)
            arr.append(distance)

        arr.sort()

        res = []

        for i in range(k):
            res.append(hash_map[arr[i]].pop())

        return res