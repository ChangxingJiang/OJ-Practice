import collections
import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = collections.deque(sorted(events, key=lambda x: (x[0], x[1])))

        ans = 0
        heap = []
        for i in range(1, 10001):
            while events and events[0][0] == i:
                heapq.heappush(heap, events.popleft()[1])
            while heap and heap[0] < i:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                ans += 1
            if not events and not heap:
                break

        return ans


if __name__ == "__main__":
    print(Solution().maxEvents(events=[[1, 2], [2, 3], [3, 4]]))  # 3
    print(Solution().maxEvents(events=[[1, 2], [2, 3], [3, 4], [1, 2]]))  # 4
    print(Solution().maxEvents(events=[[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]))  # 4
    print(Solution().maxEvents(events=[[1, 100000]]))  # 1
    print(Solution().maxEvents(events=[[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]))  # 7

    # 18
    print(Solution().maxEvents(
        events=[[27, 27], [8, 10], [9, 11], [20, 21], [25, 29], [17, 20], [12, 12], [12, 12], [10, 14], [7, 7], [6, 10],
                [7, 7], [4, 8], [30, 31], [23, 25], [4, 6], [17, 17], [13, 14], [6, 9], [13, 14]]))
