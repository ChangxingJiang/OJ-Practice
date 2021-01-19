import heapq
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1], x[2]))
        heap = []
        now = 0
        for num, start, end in trips:
            while heap and heap[0][0] <= start:
                now -= heap[0][1]
                heapq.heappop(heap)
            now += num
            if now > capacity:
                return False
            heapq.heappush(heap, (end, num))
        return True


if __name__ == "__main__":
    print(Solution().carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=4))  # False
    print(Solution().carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=5))  # True
    print(Solution().carPooling(trips=[[2, 1, 5], [3, 5, 7]], capacity=3))  # True
    print(Solution().carPooling(trips=[[3, 2, 7], [3, 7, 9], [8, 3, 9]], capacity=11))  # True
