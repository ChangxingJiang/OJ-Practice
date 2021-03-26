# LeetCode题解(0048)：旋转图像(Python)

题目：[原题链接](https://leetcode-cn.com/problems/rotate-image/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 60ms (7.76%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一：

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = [list(col)[::-1] for col in zip(*matrix)]
```