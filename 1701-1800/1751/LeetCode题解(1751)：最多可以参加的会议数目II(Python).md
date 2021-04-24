# LeetCode题解(1751)：最多可以参加的会议数目II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-number-of-events-that-can-be-attended-ii/)（困难）

标签：二分查找、动态规划、堆

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(K×E)$   | $O(K×E)$   | 1072ms (15.43%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
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
```

