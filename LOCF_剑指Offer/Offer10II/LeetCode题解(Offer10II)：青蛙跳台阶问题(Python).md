# LeetCode题解(Offer10II)：青蛙跳台阶问题(Python)

题目：[原题链接](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/)（简单）

标签：递归、数学、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 24ms (99.87%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（动态规划）：

![LeetCode题解(Offer10II)：截图](LeetCode题解(Offer10II)：截图.png)

```python
class Solution:
    def numWays(self, n: int) -> int:
        a = 1
        b = 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b % 1000000007
```