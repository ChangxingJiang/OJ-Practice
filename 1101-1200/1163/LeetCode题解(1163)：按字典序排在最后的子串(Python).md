# LeetCode题解(1163)：按字典序排在最后的子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/last-substring-in-lexicographical-order/)（困难）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 3920ms (18.31%) |
| Ans 2 (Python) | $O(N^2)$   | $O(1)$     | 476ms (56.34%)  |
| Ans 3 (Python) |            |            |                 |

解法一（暴力解法）：

```python
class Solution:
    def lastSubstring(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            ans = max(ans, s[i:])
        return ans
```

解法二（解法一优化）：

> 测试用例中有一个特别多连续的a的用例

```python
class Solution:
    def lastSubstring(self, s: str) -> str:
        ans = s
        for i in range(1, len(s)):
            if s[i] != s[i-1]:  # 如果子串的开头和前一个字符相等的话，一定不会是解
                for j in range(len(s) - i):
                    if ans[j] < s[i + j]:
                        ans = s[i:]
                        break
                    elif ans[j] > s[i + j]:
                        break
        return ans
```