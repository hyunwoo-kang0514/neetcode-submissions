class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [float('inf')] * n
        dp[n - 1] = 0

        for i in range(n - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                next_pos = i + j

                if next_pos < n:
                    dp[i] = min(dp[i], 1 + dp[next_pos])

        return dp[0]