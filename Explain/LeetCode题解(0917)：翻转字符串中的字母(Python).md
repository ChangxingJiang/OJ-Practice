# LeetCode题解(0917)：翻转字符串中的字母(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reverse-only-letters/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (89.63%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 44ms (46.19%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双指针）：

```python
def reverseOnlyLetters(self, S: str) -> str:
    S = list(S)
    idx1 = 0
    idx2 = len(S) - 1
    while idx1 < idx2:
        if not S[idx1].isalpha():
            idx1 += 1
        elif not S[idx2].isalpha():
            idx2 -= 1
        else:
            S[idx1], S[idx2] = S[idx2], S[idx1]
            idx1 += 1
            idx2 -= 1
    return "".join(S)
```

解法二（反转指针）：

```python
def reverseOnlyLetters(self, S: str) -> str:
    idx = len(S) - 1
    ans = ""
    for s in S:
        if s.isalpha():
            while idx >= 0 and not S[idx].isalpha():
                idx -= 1
            ans += S[idx]
            idx -= 1
        else:
            ans += s
    return ans
```