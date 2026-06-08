class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True # it is duplicate
            hashset.add(num)
        return False # it is not duplicate
        
        