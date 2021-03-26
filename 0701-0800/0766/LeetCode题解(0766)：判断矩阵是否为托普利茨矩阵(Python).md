# LeetCode题解(0766)：判断矩阵是否为托普利茨矩阵(Python)

题目：[原题链接](https://leetcode-cn.com/problems/toeplitz-matrix/)（简单）

| 解法           | 时间复杂度 | 空间复杂度                        | 执行用时      |
| -------------- | ---------- | --------------------------------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(x+y)$ : x和y为矩阵的宽度和高度 | 96ms (98.08%) |
| Ans 2 (Python) |            |                                   |               |
| Ans 3 (Python) |            |                                   |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

> **【思路】**
>
> 每一条对角线的横纵坐标差是相同的

```python
def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    x = len(matrix)
    y = len(matrix[0])
    hashmap = {}
    for i in range(x):
        for j in range(y):
            n = i - j
            v = matrix[i][j]
            if n not in hashmap:
                hashmap[n] = v
            else:
                if hashmap[n] != v:
                    return False
    return True
```