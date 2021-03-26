# LeetCode题解(1332)：通过删除回文子序列将字符串删为空的次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/remove-palindromic-subsequences/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 32ms (97.61%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

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

