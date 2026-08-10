class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to add new element
            subset.append(nums[i])
            dfs(i+1)

            # decision not to add new element
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res


        