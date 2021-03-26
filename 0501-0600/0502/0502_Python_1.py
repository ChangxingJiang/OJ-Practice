import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        size = len(Profits)

        # 依据成本排序项目
        lst = [(- Profits[i], Capital[i]) for i in range(size)]
        lst.sort(key=lambda x: x[1])

        i = 0  # 当前准备添加的项目
        heap = []  # 可完成的项目堆（项目收益最大值优先）

        # 贪心选择最优项目
        for _ in range(k):
            # 将资金满足的项目添加到列表
            while i < size and lst[i][1] <= W:
                heapq.heappush(heap, lst[i])
                i += 1

            if heap:
                # 选择当前收益最高的项目
                w, c = heapq.heappop(heap)
                W += -w
            else:
                return W  # 如果没有可以选择的项目则返回当前的资本

        return W


if __name__ == "__main__":
    # 4
    print(Solution().findMaximizedCapital(k=2, W=0, Profits=[1, 2, 3], Capital=[0, 1, 1]))
