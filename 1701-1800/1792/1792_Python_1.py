import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # 计算每一个班级所能带来的增益
        classes = sorted((-((p + 1) / (t + 1) - p / t), t, p) for p, t in classes)

        while extraStudents:
            add, t, p = heapq.heappop(classes)
            heapq.heappush(classes, (-((p + 2) / (t + 2) - (p + 1) / (t + 1)), t + 1, p + 1))
            extraStudents -= 1

        ans = []
        for add, t, p in classes:
            ans.append(p / t)

        return sum(ans) / len(ans)


if __name__ == "__main__":
    print(Solution().maxAverageRatio(classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2))  # 0.78333
    print(Solution().maxAverageRatio(classes=[[2, 4], [3, 9], [4, 5], [2, 10]], extraStudents=4))  # 0.53485
