import heapq
class KthLargest(object):

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


test1 = ["KthLargest", "add", "add", "add", "add", "add"]
test2 = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

KthLargest