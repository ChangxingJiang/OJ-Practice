# LeetCode题解(1614)：计算括号的最大嵌套深度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-nesting-depth-of-the-parentheses/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (87%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        now = 0
        for ch in s:
            if ch == "(":
                now += 1
                ans = max(ans, now)
            elif ch == ")":
                now -= 1
        return ans
```

