class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        line = -1
        for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][len(matrix[0]) - 1]:   
                line = i
                break
        
        if line == -1:
            return False

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


                


        