class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort original array
        nums = sorted(nums)
        res = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l,r = i + 1, len(nums) - 1
            while l < r: 
                left, right = nums[l], nums[r]
                currSum = num + left + right
                if currSum == 0:
                    res.append([num, left, right])
                    while left == nums[l] and l < r:
                        l += 1
                elif currSum < 0:
                    l += 1
                else: 
                    r -= 1
        return res

        

        
        

        
        


                

        