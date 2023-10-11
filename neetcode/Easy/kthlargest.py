class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        #Initialize a heap with nums
        #Initialize a k
        self.minHeap, self.k = nums, k
        
        #Heapify the minheap
        heapq.heapify(self.minHeap)
        
        #Pop all minimum values until heap is of size K
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        #push the value to the heap while maintaining heap properties
        heapq.heappush(self.minHeap, val)

        #Pop the heap until it is of size K
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        #Returns the kth smallest element.
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)