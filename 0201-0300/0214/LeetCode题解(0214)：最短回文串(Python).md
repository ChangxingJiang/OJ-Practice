# LeetCode题解(0214)：通过在字符串前添加字符成为回文串的最短回文串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shortest-palindrome/)（困难）

标签：字符串、双指针、递归、KMP算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 464ms (23.10%) |
| Ans 2 (Python) | $O(N^2)$   | $O(N)$     | 44ms (98.78%)  |
| Ans 3 (Python) | $O(N)$     | $O(N)$     | 56ms (92.39%)  |

>  这道题就相当于从前往后找字符串中最长的回文串

解法一（暴力解法）：

```python
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N = len(s)
        for i in range(N, 0, -1):
            if s[:i] == s[:i][::-1]:
                return s[i:][::-1] + s[:i] + s[i:]
        return ""
```

解法二（双指针递归）：

> 虽然最坏情况的时间复杂度没有变，但是平均情况的时间复杂度明显下降。

```python
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N = len(s)
        idx1 = 0
        for idx2 in range(N - 1, -1, -1):
            if s[idx1] == s[idx2]:
                idx1 += 1
        if idx1 == N:
            return s
        return s[idx1:][::-1] + self.shortestPalindrome(s[:idx1]) + s[idx1:]
```

解法三（KMP算法）：

> [KMP算法概述](https://leetcode-cn.com/problems/shortest-palindrome/solution/zui-duan-hui-wen-chuan-by-leetcode/)

```python
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s_new = s + "#" + s[::-1]
        N = len(s_new)

        table = [0] * N  # KMP失败函数
        length = 0  # 当前匹配字符串长度
        i = 1  # 当前坐标
        while i < N:
            if s_new[length] == s_new[i]:
                length += 1
                table[i] = length
                i += 1
            else:
                if length > 0:
                    length = table[length - 1]
                else:
                    i += 1
                    length = 0

        return s[table[-1]:][::-1] + s
```