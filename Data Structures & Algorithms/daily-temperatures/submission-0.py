class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brut force approach
        arr = []
        for i in range(len(temperatures)):
            currDay = temperatures[i]
            dayAfter = 0
            exist = False 
            for j in range(i + 1, len(temperatures)):
                laterDay = temperatures[j]
                if laterDay > currDay:
                    exist = True
                    dayAfter = j - i
                    break
            if exist:
                arr.append(dayAfter)
            else: 
                arr.append(0)
        return arr

        