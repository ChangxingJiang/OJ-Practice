import heapq
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heapq.heapify(arr)
        return heapq.nsmallest(k, arr)


if __name__ == "__main__":
    # [1,2] 或者 [2,1]
    print(Solution().getLeastNumbers(arr=[3, 2, 1], k=2))

    # [0]
    print(Solution().getLeastNumbers(arr=[0, 1, 2, 1], k=1))
