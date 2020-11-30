# LeetCode题解(面试17.06)：2出现的次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-2s-in-range-lcci/)（困难）

标签：数学、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 36ms (80.61%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        ans = 0

        # 当前计算位
        now = 1
        while n > now:
            last1, last2 = 2 * now, 3 * now
            now *= 10
            a, b = divmod(n, now)

            ans += a * (last2 - last1)

            if last2 <= b:
                ans += last2 - last1
            elif last1 <= b < last2:
                ans += b - last1 + 1

        return ans
```