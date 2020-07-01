import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        if len(nums) == k - 1:
            self.heap = nums + [float("-inf")]
        else:
            self.heap = nums

        heapq.heapify(self.heap)

        print(self.heap)
        for _ in range(len(nums) - k):
            heapq.heappop(self.heap)
        print(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        heapq.heappop(self.heap)
        print(self.heap)
        return self.heap[0]


if __name__ == "__main__":
    k = 3
    arr = [4, 5, 8, 2]
    kthLargest = KthLargest(3, arr)
    print(kthLargest.add(3))  # 4
    print(kthLargest.add(5))  # 5
    print(kthLargest.add(10))  # 5
    print(kthLargest.add(9))  # 8
    print(kthLargest.add(4))  # 8
