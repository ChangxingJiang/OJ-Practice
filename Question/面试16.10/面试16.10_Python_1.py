import heapq
from typing import List


class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        size = len(birth)
        people = [(birth[i], death[i]) for i in range(size)]
        people.sort()

        max_idx, max_val = 0, 0

        heap = []
        for b, d in people:
            while heap and heap[0] < b:
                heapq.heappop(heap)

            heapq.heappush(heap, d)
            if len(heap) > max_val:
                max_idx, max_val = b, len(heap)

        return max_idx


if __name__ == "__main__":
    # 1901
    print(Solution().maxAliveYear([1900, 1901, 1950], [1948, 1951, 2000]))

    # 1960
    print(Solution().maxAliveYear(
        [1972, 1908, 1915, 1957, 1960, 1948, 1912, 1903, 1949, 1977, 1900, 1957, 1934, 1929, 1913, 1902, 1903, 1901],
        [1997, 1932, 1963, 1997, 1983, 2000, 1926, 1962, 1955, 1997, 1998, 1989, 1992, 1975, 1940, 1903, 1983, 1969]))
