# LeetCode题解(1317)：将整数转换为两个无零整数的和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(1)$     | 36ms (90.49%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力枚举法）：

```python
def getNoZeroIntegers(self, n: int) -> List[int]:
    for i in range(n):
        if "0" not in str(i) and "0" not in str(n - i):
            return [i, n - i]
```

