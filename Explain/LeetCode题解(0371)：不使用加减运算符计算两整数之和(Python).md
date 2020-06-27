# LeetCode题解(0371)：不使用加减运算符计算两整数之和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sum-of-two-integers/)（简单）

| 解法           | 执行用时      |
| -------------- | ------------- |
| Ans 1 (Python) | 44ms (35.50%) |
| Ans 2 (Python) | 32ms (93.96%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（非常擦边球的、不要脸的解法）：

```python
def getSum(self, a: int, b: int) -> int:
    return sum([a, b])
```

解法二（位运算）：

```python
def getSum(self, a: int, b: int) -> int:
    return ((a & b) << 1) + (a ^ b)
```