# LeetCode题解(1716)：计算力扣银行的钱(Python)

题目：[原题链接](https://leetcode-cn.com/problems/calculate-money-in-leetcode-bank/)（简单）

标签：数学、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 36ms (84.72%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def totalMoney(self, n: int) -> int:
        week, surplus = divmod(n, 7)

        # 计算整周的结果
        n1 = 21 * week + 7 * (1 + week) * week // 2

        # 计算最后一周的结果
        n2 = (week + 1 + week + surplus) * surplus // 2

        return n1 + n2
```

