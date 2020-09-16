# LeetCode题解(0476)：计算数字的补数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-complement/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时                      |
| -------------- | ---------- | ---------- | ----------------------------- |
| Ans 1 (Python) | --         | --         | 36ms (87.07%) - 48ms (21.22%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def findComplement(self, num: int) -> int:
    return int(bin(num).replace("0b", "").replace("0", "2").replace("1", "0").replace("2", "1"), base=2)
```