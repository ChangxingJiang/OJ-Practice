# LeetCode题解(1015)：可被K整除的最小整数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/smallest-integer-divisible-by-k/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(K)$     | $O(1)$     | 56ms (65.14%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1

        v = 1
        ans = 1
        while v % K != 0:
            v %= K
            v = v * 10 + 1
            ans += 1

        return ans
```

