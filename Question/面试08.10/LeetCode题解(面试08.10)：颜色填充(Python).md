# LeetCode题解(面试08.10)：图片油漆桶渲染实现(Python)

题目：[原题链接](https://leetcode-cn.com/problems/color-fill-lcci/)（简单）

标签：数组、广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (84.45%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        h = len(image)
        w = len(image[0])

        old_color = image[sr][sc]

        if old_color == newColor:
            return image

        def change(r, c):
            if image[r][c] == old_color:
                image[r][c] = newColor
                if r > 0:
                    change(r - 1, c)
                if c > 0:
                    change(r, c - 1)
                if r < h - 1:
                    change(r + 1, c)
                if c < w - 1:
                    change(r, c + 1)

        change(sr, sc)

        return image
```