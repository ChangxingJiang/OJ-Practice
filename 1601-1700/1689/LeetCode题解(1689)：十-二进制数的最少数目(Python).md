# LeetCode题解(1689)：十-二进制数的最少数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/)（中等）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 184ms (52.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0
        for ch in n:
            if int(ch) > ans:
                ans = int(ch)
        return ans
```

