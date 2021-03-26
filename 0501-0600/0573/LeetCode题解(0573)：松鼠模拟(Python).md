# LeetCode题解(0573)：松鼠模拟(Python)

题目：[原题链接](https://leetcode-cn.com/problems/squirrel-simulation/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 216ms (8.33%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        d1 = []  # 松果到树的往返的距离
        d2 = []  # 松果到松鼠+松果到树的距离的距离
        for i1, i2 in nuts:
            if 0 <= i1 < height and 0 <= i2 < width:
                d1.append((abs(i1 - tree[0]) + abs(i2 - tree[1])) * 2)
                d2.append(abs(i1 - tree[0]) + abs(i2 - tree[1]) + abs(i1 - squirrel[0]) + abs(i2 - squirrel[1]))

        ans = 0
        more = float("inf")  # 第一个捡的松果的距离变化量
        for i in range(len(d1)):
            ans += d1[i]
            more = min(more, d2[i] - d1[i])

        return ans + more
```