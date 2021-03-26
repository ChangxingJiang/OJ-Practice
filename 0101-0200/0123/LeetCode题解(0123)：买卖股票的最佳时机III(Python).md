# LeetCode题解(0123)：买卖股票的最佳时机III(Python)

题目：[原题链接](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)（困难）

标签：数组、贪心算法、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 384ms (91.51%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 计算前缀最小值
        prefix_min = []
        last = (float("inf"), -1)
        for i, price in enumerate(prices):
            if price <= last[0]:
                last = (price, i)
            prefix_min.append(last)
        # print(prefix_min)

        # 寻找最大增幅段落
        max_idx, max_val = [], 0
        for i, price in enumerate(prices):
            val = price - prefix_min[i][0]
            if val > max_val:
                max_idx, max_val = [(prefix_min[i][1], i)], val
            elif val == max_val:
                max_idx.append((prefix_min[i][1], i))
        # print(max_idx, max_val)

        # 如果有两段最大增幅且起点不同，那么他们一定不重叠
        if len(set(x for x, y in max_idx)) > 1:
            return 2 * max_val

        max_i1, max_i2 = max_idx[0]

        # 剩下的最大值要不存在于增幅段落中（反向），要不存在于增幅段落外（正向）

        # 寻找存在于增幅段落中（反向）的最大值
        prefix_max = []
        last = float("-inf")
        for i in range(max_i1, max_i2):
            last = max(last, prices[i])
            prefix_max.append(last)
        max_v1 = 0
        for i in range(max_i1, max_i2):
            max_v1 = max(max_v1, prefix_max[i - max_i1] - prices[i])
        # print("MAX1:", prefix_max, "->", max_v1)

        # 寻找存在于增幅段落左侧（正向）的最大值
        max_v2 = 0
        for i in range(0, max_i1):
            max_v2 = max(max_v2, prices[i] - prefix_min[i][0])
        # print("MAX2:", max_v2)

        # 寻找存在于增幅段落右侧（正向）的最大值
        prefix_min = []
        last = float("inf")
        for i in range(max_i2, len(prices)):
            last = min(last, prices[i])
            prefix_min.append(last)
        max_v3 = 0
        for i in range(max_i2, len(prices)):
            max_v3 = max(max_v3, prices[i] - prefix_min[i - max_i2])
        # print("MAX3:", prefix_min, "->", max_v3)

        return max_val + max(max_v1, max_v2, max_v3)
```