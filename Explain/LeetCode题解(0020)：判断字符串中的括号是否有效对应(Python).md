# LeetCode题解：0020（有效的括号）

题目：[题目链接](https://leetcode-cn.com/problems/valid-parentheses/)（简单）

标签：栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 36ms (89.92%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 36ms (89.92%) |

解法一（使用列表存储当前括号状态）：

```python
def isValid(self, s: str) -> bool:

    sign_dict = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    sign_list = []
    for c in s:
        if c in ["(", "[", "{"]:
            sign_list.append(c)
        else:
            r = sign_dict[c]
            if sign_list and r == sign_list[-1]:
                sign_list.pop()
            else:
                return False

    if sign_list:
        return False
    else:
        return True
```

解法二：

```python
def isValid(self, s: str) -> bool:
    stack = []
    for c in s:
        if c == "(" or c == "[" or c == "{":
            stack.append(c)
        else:
            if not stack:
                return False
            elif c == ")" and stack[-1] != "(":
                return False
            elif c == "]" and stack[-1] != "[":
                return False
            elif c == "}" and stack[-1] != "{":
                return False
            stack.pop()
    return not stack
```



