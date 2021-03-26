# LeetCode题解(1561)：你可以获得的最大硬币数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-number-of-coins-you-can-get/)（中等）

标签：排序、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 148ms (89%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        times = len(piles) // 3

        ans = 0
        for i in range(times):
            ans += piles[2 * i + 1]
        return ans
```