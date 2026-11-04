class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        maxSum = minSum = nums[0]
        curMinSum = curMaxSum = 0

        for n in nums:
            curMaxSum = max(n, curMaxSum + n)
            maxSum = max(maxSum, curMaxSum)

            curMinSum = min(n, curMinSum + n)
            minSum = min(minSum, curMinSum)

            total += n
            
        if maxSum < 0:
            return maxSum
    
        return max(maxSum, total - minSum)
            
        