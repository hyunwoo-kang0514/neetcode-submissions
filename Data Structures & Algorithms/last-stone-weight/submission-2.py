class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap) # O(N)

        while len(maxHeap) > 1: # O(N)
            largest = heapq.heappop(maxHeap) # O(logN)
            secondLargest = heapq.heappop(maxHeap) # O(logN)
            # pop two elements
            if secondLargest == largest:
                continue
            else:
                heapq.heappush(maxHeap, (largest - secondLargest)) # O(longN)
        
        return -maxHeap[0] if maxHeap else 0


            


        