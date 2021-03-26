# LeetCode题解(0054)：螺旋矩阵(Python)

题目：[原题链接](https://leetcode-cn.com/problems/spiral-matrix/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(X×Y)$   | $O(1)$     | 36ms (85.56%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 处理空表的情况
        if not matrix or not matrix[0]:
            return []

        # 定义边缘位置
        top, right, bottom, left = 0, len(matrix[0]) - 1, len(matrix) - 1, 0
        stat = 0
        x, y = 0, 0
        ans = []

        while top <= bottom and left <= right:
            ans.append(matrix[x][y])
            if stat == 0:  # 向右移动的状态
                if y < right:
                    y += 1
                else:
                    top += 1
                    stat = (stat + 1) % 4
                    x += 1
            elif stat == 1:  # 向下移动的状态
                if x < bottom:
                    x += 1
                else:
                    right -= 1
                    stat = (stat + 1) % 4
                    y -= 1
            elif stat == 2:  # 向左移动的状态
                if y > left:
                    y -= 1
                else:
                    bottom -= 1
                    stat = (stat + 1) % 4
                    x -= 1
            else:  # 向上移动的状态
                if x > top:
                    x -= 1
                else:
                    left += 1
                    stat = (stat + 1) % 4
                    y += 1

        return ans
```

