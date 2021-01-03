# LeetCode题解(1691)：堆叠长方体的最大高度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-height-by-stacking-cuboids/)（困难）

标签：动态规划、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 88ms (53.44%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        cuboids = [list(sorted(cuboid, reverse=True)) for cuboid in cuboids]
        cuboids.sort(reverse=True)

        # print(cuboids)

        size = len(cuboids)

        dp = [cuboids[i][0] for i in range(size)]

        for i in range(size):
            x1, y1, z1 = cuboids[i]
            for j in range(i):
                x2, y2, z2 = cuboids[j]
                if x1 <= x2 and y1 <= y2 and z1 <= z2:
                    dp[i] = max(dp[i], dp[j] + x1)

        return max(dp)
```

