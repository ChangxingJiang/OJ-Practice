import bisect
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # 按工作难度排序，并计算每个工作难度的最大收益
        size = len(difficulty)
        lst = [(difficulty[i], profit[i]) for i in range(size)]
        lst.sort()
        for i in range(size):
            difficulty[i] = lst[i][0]
            profit[i] = lst[i][1] if i == 0 or profit[i - 1] < lst[i][1] else profit[i - 1]

        # 计算每个工人的最大收益
        ans = 0
        for work in worker:
            idx = bisect.bisect_right(difficulty, work) - 1
            if idx >= 0:
                ans += profit[idx]
        return ans


if __name__ == "__main__":
    # 100
    print(Solution().maxProfitAssignment(difficulty=[2, 4, 6, 8, 10], profit=[10, 20, 30, 40, 50], worker=[4, 5, 6, 7]))

    # 0
    print(Solution().maxProfitAssignment(difficulty=[85, 47, 57], profit=[24, 66, 99], worker=[40, 25, 25]))
