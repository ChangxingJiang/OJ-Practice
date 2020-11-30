import heapq
from typing import List


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        return heapq.nsmallest(k, arr)


if __name__ == "__main__":
    # [1,2,3,4]
    print(Solution().smallestK(arr=[1, 3, 5, 7, 2, 4, 6, 8], k=4))
