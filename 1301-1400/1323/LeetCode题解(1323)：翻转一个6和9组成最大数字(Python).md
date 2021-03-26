# LeetCode题解(1323)：翻转一个6和9组成最大数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-69-number/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(logN)$  | 28ms (98.73%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def maximum69Number(self, num: int) -> int:
    s = str(num)
    if "6" not in s:
        return num
    else:
        i = s.index("6")
        return num + 3 * (10 ** (len(s) - i - 1))
```