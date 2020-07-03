# LeetCode题解(1137)：计算斐波那契数列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/n-th-tribonacci-number/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (37.23%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 36ms (85.09%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（迭代法）：

```python
def tribonacci(self, n: int) -> int:
    ans = [0, 1, 1]
    for i in range(3, n + 1):
        ans.append(ans[-3] + ans[-2] + ans[-1])
    return ans[n]
```

解法二（优化存储方法）：

```python
def tribonacci(self, n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    x1 = 0
    x2 = 1
    x3 = 1
    for i in range(3, n + 1):
        x1, x2, x3 = x2, x3, x1 + x2 + x3
    return x3
```