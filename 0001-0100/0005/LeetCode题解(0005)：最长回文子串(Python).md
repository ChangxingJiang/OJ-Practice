# LeetCode题解(0005)：字符串中的最长回文子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-palindromic-substring/)（中等）

标签：字符串、字符串-切片器、双指针、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 1068ms (76.30%) |
| Ans 2 (Python) | $O(N^2)$   | $O(1)$     | 60ms (99.80%)   |
| Ans 3 (Python) |            |            |                 |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（朴素的暴力解法——中心扩散解法）：

```python
def longestPalindrome(self, s: str) -> str:
    ans = ""
    for i in range(len(s)):
        m = i - 1
        n = i
        while m >= 0 and n < len(s) and s[m] == s[n]:
            m -= 1
            n += 1
        if n - m - 1 > len(ans):
            ans = s[m + 1:n]
        m = i
        n = i
        while m >= 0 and n < len(s) and s[m] == s[n]:
            m -= 1
            n += 1
        if n - m - 1 > len(ans):
            ans = s[m + 1:n]
    return ans
```

解法二（使用切片器比较字符串）：

![LeetCode题解(0005)：截图1](LeetCode题解(0005)：截图1.png)

```python
def longestPalindrome(self, s: str) -> str:
    length = 0
    start = 0
    for i in range(len(s)):
        t = s[i - length - 1:i + 1]
        if i - length - 1 >= 0 and t == t[::-1]:
            start = i - length - 1
            length += 2
            continue
        t = s[i - length:i + 1]
        if i - length >= 0 and t == t[::-1]:
            start = i - length
            length += 1
    return s[start:start + length]
```