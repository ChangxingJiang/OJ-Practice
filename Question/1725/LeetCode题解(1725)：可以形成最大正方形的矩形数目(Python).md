# LeetCode题解(1725)：可以形成最大正方形的矩形数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-rectangles-that-can-form-the-largest-square/)（简单）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 52ms (74.05%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_val, max_num = 0, 0
        for l, w in rectangles:
            if l < w:
                l, w = w, l
            if w > max_val:
                max_val, max_num = w, 1
            elif w == max_val:
                max_num += 1
        return max_num
```

