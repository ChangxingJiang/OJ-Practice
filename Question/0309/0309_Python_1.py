import collections
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        # 计算所有差值
        differ1 = collections.deque([prices[i + 1] - prices[i] for i in range(len(prices) - 1)])

        # 去掉首尾的跌幅
        while differ1 and differ1[0] < 0:
            differ1.popleft()
        while differ1 and differ1[-1] < 0:
            differ1.pop()

        print(differ1)

        # 去掉所有连续跌幅（超过2个连续跌幅中间卖掉冷冻期不影响）
        differ2 = []
        last = False  # 之前是否是连续跌幅
        for differ in differ1:
            if differ >= 0:
                differ2.append(differ)
                last = False
            else:
                if last:
                    continue
                elif differ2 and differ2[-1] < 0:
                    differ2.pop()
                    last = True
                else:
                    differ2.append(differ)

        print(differ2)

        if not differ2:
            return 0

        early1, early2 = 0, 0  # 更早的最大值
        last = 0  # 上一个数的最大值
        for i in range(len(differ2)):
            early2, early1, last = max(early2, early1), last, last + differ2[i]
            last = max(last, early2)

        return last



if __name__ == "__main__":
    print(Solution().maxProfit([1, 2, 3, 0, 2]))  # 3
    print(Solution().maxProfit([2, 6, 8, 7, 8, 7, 9, 4, 1, 2, 4, 5, 8]))  # 15

    # 自制用例
    print(Solution().maxProfit([1, 2]))  # 1
