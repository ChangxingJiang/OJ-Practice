# LeetCode题解(0867)：转置矩阵(Python)

题目：[原题链接](https://leetcode-cn.com/problems/transpose-matrix/)（简单）

| 解法           | 时间复杂度                         | 空间复杂度                         | 执行用时       |
| -------------- | ---------------------------------- | ---------------------------------- | -------------- |
| Ans 1 (Python) | $O(X×Y)$ : X和Y为矩阵A的宽度和高度 | $O(X×Y)$ : X和Y为矩阵A的宽度和高度 | 88ms (81.65%)  |
| Ans 2 (Python) | $O(X×Y)$ : X和Y为矩阵A的宽度和高度 | $O(X×Y)$ : X和Y为矩阵A的宽度和高度 | 100ms (31.65%) |
| Ans 3 (Python) |                                    |                                    |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def transpose(self, A: List[List[int]]) -> List[List[int]]:
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
```

解法二：

```python
def transpose(self, A: List[List[int]]) -> List[List[int]]:
    x = len(A)
    y = len(A[0])
    ans = []
    for j in range(y):
        line = []
        for i in range(x):
            line.append(A[i][j])
        ans.append(line)
    return ans
```