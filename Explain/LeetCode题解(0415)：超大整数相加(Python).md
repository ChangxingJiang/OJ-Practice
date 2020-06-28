# LeetCode题解(0415)：超大整数相加(Python)

题目：[原题链接](https://leetcode-cn.com/problems/add-strings/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | O(n+m)     | 60ms (52.23%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def addStrings(self, num1: str, num2: str) -> str:
    num1 = num1.zfill(len(num2))
    num2 = num2.zfill(len(num1))
    carry = 0
    ans = []
    for i in range(1, len(num1) + 1):
        n1 = int(num1[-i])
        n2 = int(num2[-i])
        n = n1 + n2 + carry
        ans.append(str(n % 10))
        carry = n // 10
    if carry == 1:
        ans.append("1")
    ans.reverse()
    return "".join(ans)
```

