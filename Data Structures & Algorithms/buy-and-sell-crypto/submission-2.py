class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else: # in this case, we can calculate the price
                currP = prices[r] - prices[l]
                maxP = max(currP, maxP)
            r += 1
        return maxP





        