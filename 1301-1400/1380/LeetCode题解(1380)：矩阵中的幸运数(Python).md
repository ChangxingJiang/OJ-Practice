# LeetCode题解(1380)：矩阵中的幸运数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix/)（简单）

| 解法           | 时间复杂度                            | 空间复杂度 | 执行用时      |
| -------------- | ------------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2×M)$ : N为矩阵行数，M为矩阵列数 | $O(1)$     | 48ms (84.94%) |
| Ans 2 (Python) | $O(N×M)$: N为矩阵行数，M为矩阵列数    | $O(N+M)$   | 84ms (14.77%) |
| Ans 3 (Python) |                                       |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法A）：

```python
def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
    x = len(matrix)
    y = len(matrix[0])
    ans = []
    for i in range(x):
        min_num = float("inf")
        min_idx = -1
        for j in range(y):
            if matrix[i][j] < min_num:
                min_num = matrix[i][j]
                min_idx = j
        for k in range(x):
            if matrix[k][min_idx] > min_num:
                break
        else:
            ans.append(min_num)
    return ans
```

解法二（暴力解法B）：

```python
def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
    x = len(matrix)
    y = len(matrix[0])
    min_r = [float("inf")] * x
    max_c = [float("-inf")] * y
    for i in range(x):
        for j in range(y):
            min_r[i] = min(min_r[i], matrix[i][j])
            max_c[j] = max(max_c[j], matrix[i][j])

    ans = []
    for i in range(x):
        for j in range(y):
            if matrix[i][j] == min_r[i] == max_c[j]:
                ans.append(matrix[i][j])
    return ans
```