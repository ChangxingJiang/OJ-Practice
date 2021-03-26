# LeetCode题解(0302)：包含全部黑色像素的最小矩形(Python)

题目：[原题链接](https://leetcode-cn.com/problems/smallest-rectangle-enclosing-black-pixels/)（困难）

标签：广度优先搜索、深度优先搜索、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×M)$   | $O(N×M)$   | 600ms (12.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（广度优先搜索）：

```python
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        def is_valid(x, y):
            return 0 <= x < s1 and 0 <= y < s2

        def get_near(x, y):
            res = []
            for xx, yy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if is_valid(xx, yy):
                    res.append((xx, yy))
            return res

        s1, s2 = len(image), len(image[0])

        min_x, min_y, max_x, max_y = x, y, x, y
        visited = set()
        queue = collections.deque([(x, y)])
        while queue:
            x1, y1 = queue.popleft()
            for x2, y2 in get_near(x1, y1):
                if image[x2][y2] == "1" and (x2, y2) not in visited:
                    visited.add((x2, y2))
                    queue.append((x2, y2))
                    min_x, max_x = min(min_x, x2), max(max_x, x2)
                    min_y, max_y = min(min_y, y2), max(max_y, y2)

        return (max_x - min_x + 1) * (max_y - min_y + 1)
```