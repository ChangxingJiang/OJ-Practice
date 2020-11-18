# LeetCode题解(面试01.06)：依据指定规则压缩字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/compress-string-lcci/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 64ms (55.70%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return S

        N = []
        last, start = S[0], 0
        for i, ch in enumerate(S[1:]):
            if ch != last:
                N.append(last + str(i + 1 - start))
                last, start = ch, i + 1
        else:
            N.append(last + str(len(S) - start))

        N = "".join(N)

        if len(S) <= len(N):
            return S
        else:
            return N
```