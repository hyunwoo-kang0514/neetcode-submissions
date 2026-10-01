class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            largest = heapq.heappop(maxHeap)
            secondLargest = heapq.heappop(maxHeap)
            # pop two elements
            if secondLargest == largest:
                continue
            else:
                heapq.heappush(maxHeap, (largest - secondLargest))
        
        return -maxHeap[0] if maxHeap else 0


            


        