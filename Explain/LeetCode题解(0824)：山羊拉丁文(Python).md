# LeetCode题解(0824)：山羊拉丁文(Python)

题目：[原题链接](https://leetcode-cn.com/problems/goat-latin/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 36ms (87.10%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def toGoatLatin(self, S: str) -> str:
    S = S.split(" ")
    ans = []
    for i in range(len(S)):
        s = S[i]
        if s[0] not in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
            s = s[1:] + s[0]
        s += "m" + "a" * (i + 2)
        ans.append(s)
    return " ".join(ans)
```