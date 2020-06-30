# LeetCode题解(0633)：平方数之和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sum-of-square-numbers/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 超出时间限制   |
| Ans 2 (Python) | $O(NlogN)$ | $O(1)$     | 320ms (51.58%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def judgeSquareSum(self, c: int) -> bool:
    half = int(pow(c, 0.5) + 1)
    for i in range(half):
        for j in range(half):
            if pow(i, 2) + pow(j, 2) == c:
                return True
    else:
        return False
```

解法二：

```python
def judgeSquareSum(self, c: int) -> bool:
    half = int(pow(c, 0.5) + 1)
    for i in range(0, half):
        if pow(c - pow(i, 2), 0.5) % 1 == 0:
            return True
    else:
        return False
```