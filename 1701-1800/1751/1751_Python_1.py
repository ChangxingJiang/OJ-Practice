import heapq
from typing import List


# 1 <= startDayi <= endDayi <= 10^9  # 不可能按天遍历
# 1 <= k * events.length <= 10^6  # 最高复杂度就是k*events.length


class Solution:
    def maxValue(self, events: List[List[int]], total: int) -> int:
        size = len(events)

        # 排序会议
        events.sort(key=lambda x: (x[0], x[1]))

        # 计算每一个会议结束时是在第几个会议之前
        time_lst = [size] * size
        heap = []
        for j in range(size):
            start, end = events[j][0:2]
            while heap and heap[0][0] < start:
                time_lst[heapq.heappop(heap)[1]] = j
            heapq.heappush(heap, (end, j))

        # print("会议时间列表:", time_lst)

        # 动态规划计算最优解
        dp = [[0] * (total + 1) for _ in range(size + 1)]  # dp[i][j] = 在第i个结束的时间里，最多参加j个会议的最大价值

        for i in range(size):
            j = time_lst[i]
            value = events[i][2]

            # 寻找参加当前会议之前的最大值
            if i > 0:
                for k in range(1, total + 1):
                    dp[i][k] = max(dp[i][k], dp[i - 1][k])

            # 选择当前会议的情况
            for k in range(total):
                dp[j][k + 1] = max(dp[j][k + 1], dp[j - 1][k + 1], dp[i][k] + value)

        # for row in dp:
        #     print(row)

        return max(dp[size])


if __name__ == "__main__":
    print(Solution().maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 1]], total=2))  # 7
    print(Solution().maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 10]], total=2))  # 10
    print(Solution().maxValue(events=[[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], total=3))  # 9

    # 测试用例 25/66
    print(Solution().maxValue(events=[[1, 3, 4], [2, 4, 1], [1, 1, 4], [3, 5, 1], [2, 5, 5]], total=3))  # 9

    # 自制测试用例
    print(Solution().maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 6]], total=2))  # 7
    print(Solution().maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 5], [4, 4, 1]], total=2))  # 7
