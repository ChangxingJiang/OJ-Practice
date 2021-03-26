# LeetCode题解(1503)：计算指定规则下所有蚂蚁掉下来前的最后一刻(Python)

题目：[原题链接](https://leetcode-cn.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/)（中等）

标签：数组、数学、脑筋急转弯

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 48ms (82%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # 处理不相遇的特殊情况
        if not left:
            return n - min(right)
        if not right:
            return max(left)

        # 处理相遇的情况
        return max(n - min(right), max(left))
```