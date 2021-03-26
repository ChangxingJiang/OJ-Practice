import bisect
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        size = len(intervals)

        # 构造起点列表
        starts = []
        for i, (l, r) in enumerate(intervals):
            starts.append((l, i))
        starts.sort()

        # 寻找结果
        ans = []
        for (l, r) in intervals:
            idx = bisect.bisect_right(starts, (r, -1))
            if idx == size and starts[idx - 1][0] < r:
                ans.append(-1)
            else:
                ans.append(starts[idx][1])
        return ans


if __name__ == "__main__":
    # [-1]
    print(Solution().findRightInterval([[1, 2]]))

    # [-1, 0, 1]
    print(Solution().findRightInterval([[3, 4], [2, 3], [1, 2]]))

    # [-1, 2, -1]
    print(Solution().findRightInterval([[1, 4], [2, 3], [3, 4]]))

    # [-1, 1, 1]
    print(Solution().findRightInterval([[4, 5], [2, 3], [1, 2]]))
