class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) # O(N)
        while len(self.minHeap) > k: # (O((n-k)logn))
            heapq.heappop(self.minHeap)
       

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # O(logN)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # O(logN)
        return self.minHeap[0]
     




        
