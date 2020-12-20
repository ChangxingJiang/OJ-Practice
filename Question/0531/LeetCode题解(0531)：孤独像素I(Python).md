# LeetCode题解(0531)：孤独像素I(Python)

题目：[原题链接](https://leetcode-cn.com/problems/lonely-pixel-i/)（中等）

标签：数组、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×M)$   | $O(N×M)$   | 76ms (97.67%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        count_row = []
        for row in picture:
            count_row.append(row.count("B"))

        count_col = []
        for col in zip(*picture):
            count_col.append(col.count("B"))

        ans = 0

        for i in range(len(picture)):
            if count_row[i] == 1:
                for j in range(len(picture[i])):
                    if picture[i][j] == "B" and count_col[j] == 1:
                        ans += 1

        return ans
```