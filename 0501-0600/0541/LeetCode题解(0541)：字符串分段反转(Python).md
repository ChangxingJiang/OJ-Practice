# LeetCode题解(0541)：字符串分段反转(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reverse-string-ii/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 32ms (97.78%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def reverseStr(self, s: str, k: int) -> str:
    ans = ""
    while k * 2 <= len(s):
        ans += s[0:k][::-1]
        ans += s[k:k * 2]
        s = s[k * 2:]
    else:
        if k <= len(s):
            ans += s[0:k][::-1]
            ans += s[k:]
        else:
            ans += s[::-1]
    return ans
```