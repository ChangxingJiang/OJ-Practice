# LeetCode题解(1009)：十进制整数的反码(Python)

题目：[原题链接](https://leetcode-cn.com/problems/complement-of-base-10-integer/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 32ms (95.57%) |
| Ans 2 (Python) | $O(1)$     | $O(1)$     | 36ms (85.96%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（遍历修改）：

```python
def bitwiseComplement(self, N: int) -> int:
    return int("".join("1" if i == "0" else "0" for i in bin(N)[2:]), base=2)
```

解法二（利用原码和反码相加为2**n-1）：

```python
def bitwiseComplement(self, N: int) -> int:
    return 2 ** (len(bin(N)) - 2) - 1 - N
```