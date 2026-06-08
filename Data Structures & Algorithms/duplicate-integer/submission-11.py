class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_hash = {}
        for num in nums:
            my_hash[num] = None
        for num in nums:
            if my_hash[num] == None:
                my_hash[num] = 1
            else:
                return True
        return False
        
        