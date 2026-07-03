class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        bot, top = 0, ROWS - 1
        
        while bot <= top: 
            row = (bot + top) // 2
            if target > matrix[row][-1]:
                bot = row + 1
            elif target < matrix[row][0]:
                top = row - 1
            else: 
                break 
    
        if bot > top:
            return False
        line = row
        l, r = 0, len(matrix[line]) - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[line][m] > target:
                r = m - 1
            elif matrix[line][m] < target:
                l = m + 1
            else:
                return True
        return False


                


        