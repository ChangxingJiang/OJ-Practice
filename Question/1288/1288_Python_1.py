from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        ans = len(intervals)

        most_right = 0
        for left, right in intervals:
            if right <= most_right:
                ans -= 1
            else:
                most_right = right

        return ans


if __name__ == "__main__":
    print(Solution().removeCoveredIntervals(intervals=[[1, 4], [3, 6], [2, 8]]))  # 2
    print(Solution().removeCoveredIntervals(intervals=[[1, 2], [1, 4], [3, 4]]))  # 1
