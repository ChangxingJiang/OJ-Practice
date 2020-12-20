# LeetCode题解(1523)：在区间范围内统计奇数数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-odd-numbers-in-an-interval-range/)（简单）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 44ms (33.75%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (high - low) % 2 == 1:
            return (high - low) // 2 + 1
        else:
            ans = (high - low) // 2
            ans += 1 if high % 2 == 1 and low % 2 == 1 else 0
            return ans
```