import heapq
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_heap, max_heap = [], []
        for i, array in enumerate(arrays):
            heapq.heappush(min_heap, (min(array), i))
            heapq.heappush(max_heap, (-max(array), i))

        min1, i1 = heapq.heappop(min_heap)
        max1, i2 = heapq.heappop(max_heap)
        min2, i3 = heapq.heappop(min_heap)
        max2, i4 = heapq.heappop(max_heap)
        if i1 != i2:
            return (-max1) - min1
        else:
            return max((-max2) - min1, (-max1) - min2)


if __name__ == "__main__":
    # 4
    print(Solution().maxDistance([[1, 2, 3],
                                  [4, 5],
                                  [1, 2, 3]]))
