import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []  # 结束时间堆
        ans = 0
        for interval in intervals:
            left, right = interval
            while heap and heap[0] <= left:
                heapq.heappop(heap)
            heapq.heappush(heap, right)
            ans = max(ans, len(heap))
        return ans


if __name__ == "__main__":
    print(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]))  # 2
    print(Solution().minMeetingRooms([[7, 10], [2, 4]]))  # 1
