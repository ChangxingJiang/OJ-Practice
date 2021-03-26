import collections
import heapq
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = collections.Counter(barcodes)
        heap = [(-v, k) for k, v in count.items()]
        heapq.heapify(heap)

        ans = []
        last = None
        while heap:
            v1, k1 = heapq.heappop(heap)
            if k1 != last:
                ans.append(k1)
                last = k1
                if v1 + 1 < 0:
                    heapq.heappush(heap, (v1 + 1, k1))
            else:
                v2, k2 = heapq.heappop(heap)
                ans.append(k2)
                last = k2
                heapq.heappush(heap, (v1, k1))
                if v2 + 1 < 0:
                    heapq.heappush(heap, (v2 + 1, k2))
        return ans


if __name__ == "__main__":
    # [2,1,2,1,2,1]
    print(Solution().rearrangeBarcodes([1, 1, 1, 2, 2, 2]))

    # [1,3,1,3,2,1,2,1]
    print(Solution().rearrangeBarcodes([1, 1, 1, 1, 2, 2, 3, 3]))
