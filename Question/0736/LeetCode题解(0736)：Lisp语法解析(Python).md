# LeetCode题解(0736)：Lisp语法表达式解析(Python)

题目：[原题链接](https://leetcode-cn.com/problems/parse-lisp-expression/)（困难）

标签：字符串、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (97.06%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def evaluate(self, expression: str) -> int:
        value_stack = [[]]  # 表达式数据栈
        param_stack = [{}]  # 表达式参数栈
        for elem in expression.replace("(", "( ").replace(")", " )").split():
            if elem == "(":
                value_stack.append([])
                param_stack.append(param_stack[-1].copy())
            elif elem == ")":
                values = value_stack.pop()
                if values[0] == "add":
                    value = values[1] + values[2]
                elif values[0] == "mult":
                    value = values[1] * values[2]
                else:
                    if isinstance(values[1], int):
                        value = values[1]
                    elif values[1].isdigit() or (values[1][0] == "-" and values[1][1:].isdigit()):
                        value = int(values[1])
                    else:
                        value = param_stack[-1][values[1]]
                value_stack[-1].append(value)
                param_stack.pop()
                if value_stack[-1][0] == "let" and len(value_stack[-1]) % 2 == 1:
                    value = value_stack[-1].pop()
                    param_stack[-1][value_stack[-1].pop()] = value
            else:
                if not value_stack[-1]:
                    value_stack[-1].append(elem)
                elif value_stack[-1][0] == "let":
                    if len(value_stack[-1]) % 2 == 0:
                        if elem.isdigit() or (elem[0] == "-" and elem[1:].isdigit()):
                            param_stack[-1][value_stack[-1].pop()] = int(elem)
                        else:
                            param_stack[-1][value_stack[-1].pop()] = param_stack[-1][elem]
                    else:
                        value_stack[-1].append(elem)
                else:
                    if elem.isdigit() or (elem[0] == "-" and elem[1:].isdigit()):
                        value_stack[-1].append(int(elem))
                    else:
                        value_stack[-1].append(param_stack[-1][elem])
            # print(elem, "->", value_stack, param_stack)
        return value_stack[0][0]
```

