# LeetCode题解(1332)：删除回文子序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/remove-palindromic-subsequences/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 32ms (97.61%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（在同时包括a和b且不回文的情况下， 字符串中所有a和所有b所组成的子序列总是回文）：

```python
def removePalindromeSub(self, s: str) -> int:
    if "a" in s and "b" in s and s != s[::-1]:
        return 2
    elif len(s) > 0:
        return 1
    else:
        return 0
```

