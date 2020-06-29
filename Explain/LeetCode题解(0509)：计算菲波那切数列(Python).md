# LeetCode题解(0509)：计算菲波那切数列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/fibonacci-number/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(n)       | O(1)       | 28ms (99.33%) |
| Ans 2 (Python) | O(1)       | O(1)       | 28ms (99.33%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（迭代法）：

```python
def fib(self, N: int) -> int:
    if N == 0:
        return 0
    if N == 1:
        return 1
    
    x1 = 0
    x2 = 1
    for _ in range(1, N):
        x1, x2 = x2, x1 + x2

    return x2
```

解法二（通项公式）：

```python
def fib(self, N: int) -> int:
    x = (1 + 5 ** 0.5) / 2
    return int((x ** N + 1) / 5 ** 0.5)
```