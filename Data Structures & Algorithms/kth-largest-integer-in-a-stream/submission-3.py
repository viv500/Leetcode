import heapq
class KthLargest:

    # note: keep heap size at k
    # note: despite "largest", still use a min heap
    # cuz we don't wanna heap pop the largest values, only the smallest

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)

        self.heap = nums
        self.k = k

        # the init could be a list larger than k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heap = self.heap
        k = self.k

        # case 1: space -> add new value
        # case 2: no space + new value larger than min value -> add new value pop smallest
        # case 3: no space + new value smaller -> don't add as it doesn't affect kth largest
        if len(heap) < k:
            heapq.heappush(heap, val)
        elif val > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, val)

        return heap[0]
        
