# LeetCode题解(0693)：判断整数是否为交替位二进制数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-number-with-alternating-bits/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 32ms (94.29%) |
| Ans 2 (Python) | $O(1)$     | $O(1)$     | 36ms (84.38%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def hasAlternatingBits(self, n: int) -> bool:
    n = bin(n)
    return "11" not in n and "00" not in n
```

解法二（位运算）：

```python
def hasAlternatingBits(self, n: int) -> bool:
    n = n ^ (n << 1)  # -> 1...10 or 1...11
    n = n >> 1  # -> 1..11
    return n & (n + 1) == 0
```