class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for temperature in temperatures:
            res.append(0)

        for i, temperature in enumerate(temperatures):
            # 여기서 지금 문제가 stack은 key value인데 stack[-1]는 dict이다.
            if not stack or stack and temperature < next(iter(stack[-1])):
                stack.append({temperature : i})
                continue
            while stack and temperature > next(iter(stack[-1])):
                item = stack.pop()
                idx = item[next(iter(item))]
                res[idx] = i - idx
            stack.append({temperature : i})
        return res



        """
                               0. 1. 2. 3. 4. 5. 6. 
        Input: temperatures = [30,38,30,36,35,40,28]
        stack = [(40, 5), (28)]
        res = [1, 4, 1, 2, 1, 0, 0]

        """


                
                

       



        