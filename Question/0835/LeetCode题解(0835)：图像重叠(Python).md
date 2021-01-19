# LeetCode题解(0835)：图像重叠(Python)

题目：[原题链接](https://leetcode-cn.com/problems/image-overlap/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^4)$   | $O(1)$     | 2312ms (14.12%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一（极致暴力）：

```python
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        size = len(img1)

        def count(di, dj):
            res = 0
            for i2 in range(size):
                for j2 in range(size):
                    if 0 <= i2 + di < size and 0 <= j2 + dj < size and img1[i2 + di][j2 + dj] == img2[i2][j2] == 1:
                        res += 1
            return res

        ans = 0
        for i1 in range(-size + 1, size):
            for j1 in range(-size + 1, size):
                ans = max(ans, count(i1, j1))
        return ans
```

