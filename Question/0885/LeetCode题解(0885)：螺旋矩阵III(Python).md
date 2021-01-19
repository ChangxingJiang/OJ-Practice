# LeetCode题解(0885)：螺旋矩阵III(Python)

题目：[原题链接](https://leetcode-cn.com/problems/spiral-matrix-iii/)（中等）

标签：数组、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(R×C)$   | $O(1)$     | 116ms (80.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # 定义边缘位置
        top, bottom, left, right = r0, r0, c0, c0 + 1
        stat = 0
        x, y = r0, c0

        ans = []

        while len(ans) < R * C:
            if 0 <= x < R and 0 <= y < C:
                ans.append([x, y])
            if stat == 0:  # 向右移动的状态
                if y < right:
                    y += 1
                else:
                    bottom += 1
                    stat = 1
                    x += 1
            elif stat == 1:  # 向下移动的状态
                if x < bottom:
                    x += 1
                else:
                    left -= 1
                    stat = 2
                    y -= 1
            elif stat == 2:  # 向左移动的状态
                if y > left:
                    y -= 1
                else:
                    top -= 1
                    stat = 3
                    x -= 1
            else:  # 向上移动的状态
                if x > top:
                    x -= 1
                else:
                    right += 1
                    stat = 0
                    y += 1

        return ans
```

