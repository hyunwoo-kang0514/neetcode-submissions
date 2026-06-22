class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        # maintain right one big or equal to the left one
        while l < r:
            left, right = heights[l], heights[r]
            area = abs(r-l) * min(left, right)
            res = max(res, area)
            if right > left:
                l += 1
            elif left > right:
                r -= 1
            else: 
                r -= 1
        return res





        