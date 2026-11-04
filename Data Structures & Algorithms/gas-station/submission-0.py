class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            d = gas[i] - cost[i]
            total += d
            tank += d

            if tank < 0:
                tank = 0          # 1. 탱크 비우고
                start = i + 1     # 2. 다음 칸에서 새로 출발

        if total < 0:
            return -1
            
        return start