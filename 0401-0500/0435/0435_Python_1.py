from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        size = len(intervals)

        now = intervals[0][1]

        ans = size - 1

        for i in range(1, size):
            if intervals[i][0] >= now:
                ans -= 1
                now = intervals[i][1]

        return ans


if __name__ == "__main__":
    # 1
    print(Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))

    # 2
    print(Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))

    # 0
    print(Solution().eraseOverlapIntervals([[1, 2], [2, 3]]))
