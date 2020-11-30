# LeetCode题解(0939)：最小面积矩形(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-area-rectangle/)（中等）

标签：哈希表、几何

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 764ms (87.97%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ans = float("inf")
        count_x = collections.defaultdict(set)
        count_y = collections.defaultdict(set)
        for x1, y1 in points:
            for y2 in count_x[x1]:
                for x2 in count_y[y1]:
                    if x2 in count_y[y2]:
                        ans = min(ans, abs(y2 - y1) * abs(x2 - x1))
            count_x[x1].add(y1)
            count_y[y1].add(x1)
        return ans if ans != float("inf") else 0
```