# LeetCode题解(0032)：字符串中的最长有效括号子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-valid-parentheses/)（困难）

标签：字符串、栈、双指针

|      解法      | 时间复杂度 | 空间复杂度 |   执行用时    |
| :------------: | :--------: | :--------: | :-----------: |
| Ans 1 (Python) |   $O(N)$   |   $O(N)$   | 48ms (94.89%) |
| Ans 2 (Python) |   $O(N)$   |   $O(1)$   | 48ms (94.89%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（栈）：

```python
def longestValidParentheses(self, s: str) -> int:
    stack = [-1]
    ans = 0
    for i, ch in enumerate(s):
        if ch == "(":
            stack.append(i)
        else:
            if len(stack) > 1:
                stack.pop()
                ans = max(ans, i - stack[-1])
            else:
                stack[-1] = i
    return ans
```

解法二（双指针计数）：

```python
def longestValidParentheses(self, s: str) -> int:
    ans = 0

    # 正向遍历
    left = right = 0
    for ch in s:
        if ch == "(":
            left += 1
        else:
            right += 1
            if left == right:
                ans = max(ans, right * 2)
            elif left < right:
                left = 0
                right = 0

    # 反向遍历
    left = right = 0
    for ch in s[::-1]:
        if ch == "(":
            left += 1
            if left == right:
                ans = max(ans, left * 2)
            elif left > right:
                left = 0
                right = 0
        else:
            right += 1

    return ans
```