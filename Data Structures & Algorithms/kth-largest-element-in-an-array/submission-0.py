class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using max heap 
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        val = 0
        while k > 0:
            val = heapq.heappop(max_heap)
            k = k - 1
        
        return -val
            

        