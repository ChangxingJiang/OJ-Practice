# LeetCode题解(0831)：隐藏邮箱地址和电话号码个人信息(Python)

题目：[原题链接](https://leetcode-cn.com/problems/masking-personal-information/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (66.39%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
class Solution:
    def maskPII(self, S: str) -> str:
        # 处理电子邮箱的情况
        if "@" in S:
            i = S.index("@")
            S = S.lower()
            return S[0] + "*****" + S[i - 1:]

        # 处理电话的情况
        else:
            def is_digit(ch):
                return ch.isdigit()

            S = "".join(list(filter(is_digit, S)))
            if len(S) == 10:
                return "***-***-" + S[-4:]
            else:
                return "+" + "*" * (len(S) - 10) + "-***-***-" + S[-4:]
```