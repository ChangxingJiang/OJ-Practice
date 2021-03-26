# LeetCode题解(面试08.13)：堆箱子问题(Python)

题目：[原题链接](https://leetcode-cn.com/problems/pile-box-lcci/)（困难）

标签：动态规划、回溯算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 840ms (78.50%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（动态规划）：

```python
class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        # 依据长宽高总和排序箱子
        # O(NlogN)
        box.sort(key=lambda x: sum(x), reverse=True)

        # 初始化状态表格
        dp = [b[2] for b in box]

        # 状态转移
        for i in range(1, len(box)):
            w1, d1, h1 = box[i]
            max_height = 0
            for j in range(i - 1, - 1, -1):
                w2, d2, h2 = box[j]
                if w1 < w2 and d1 < d2 and h1 < h2:
                    max_height = max(max_height, dp[j])

            dp[i] = max(dp[i], max_height + h1)

        return max(dp)
```