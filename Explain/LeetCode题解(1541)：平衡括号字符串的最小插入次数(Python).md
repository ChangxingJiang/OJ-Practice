# LeetCode题解(1541)：使字符串变为平衡括号字符串的最少插入次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-insertions-to-balance-a-parentheses-string/)（中等）

标签：字符串、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 284ms (36.48%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 240ms (53.63%) |
| Ans 3 (Python) | $O(N)$     | $O(N)$     | 76ms (99.34%)  |

解法一（栈）：

```python
class Solution:
    def minInsertions(self, s: str) -> int:
        # 用栈处理可以配对的括号
        N = len(s)
        ans = 0
        stack = []
        i = 0
        while i < N:
            if s[i] == "(":
                stack.append("(")
                i += 1
            else:
                if i < len(s) - 1 and s[i + 1] == ")":
                    i += 2
                else:  # 如果不是连续的括号则补一个使其成为连续的括号
                    i += 1
                    ans += 1
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(")")

        print(ans, stack)

        # 处理未配对的括号
        n1 = stack.count("(")
        n2 = len(stack) - n1
        ans += n1 * 2
        ans += n2

        return ans
```

解法二（优化解法一）：

```python
class Solution:
    def minInsertions(self, s: str) -> int:
        N = len(s)
        ans = 0
        left_num = 0
        i = 0
        while i < N:
            if s[i] == "(":
                left_num += 1
                i += 1
            else:
                if i < len(s) - 1 and s[i + 1] == ")":
                    i += 2
                else:  # 如果不是连续的括号则补一个使其成为连续的括号
                    i += 1
                    ans += 1
                if left_num > 0:
                    left_num -= 1
                else:
                    ans += 1

        return ans + 2 * left_num
```

解法三（字符串替换）：

![LeetCode题解(1541)：截图](LeetCode题解(1541)：截图.png)

```python
class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace("))", "*")
        ans = s.count(")")
        s = s.replace(")", "*")
        while len(ss := s.replace("(*", "")) != len(s):
            s = ss
        return ans + len(s) + s.count("(")
```