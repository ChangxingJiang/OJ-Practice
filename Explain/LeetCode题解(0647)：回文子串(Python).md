# LeetCode题解(0647)：字符串的回文子串数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/palindromic-substrings/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 120ms (94.10%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)

        ans = 0

        # 处理奇数长度的回文串
        for i in range(N):
            ans += 1
            left, right = i - 1, i + 1
            while 0 <= left and right < N and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

        # 处理偶数长度的回文串
        for i in range(N - 1):
            left, right = i, i + 1
            while 0 <= left and right < N and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

        return ans
```