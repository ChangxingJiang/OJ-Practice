# LeetCode题解(1096)：按照指定语法展开字符串的花括号(Python)

题目：[原题链接](https://leetcode-cn.com/problems/brace-expansion-ii/)（困难）

标签：字符串、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 60ms (67.86%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（构造集合类）：

```python
class Expression(set):
    def __add__(self, other):
        ans = Expression()
        for elem in self:
            ans.add(elem)
        for elem in other:
            ans.add(elem)
        return ans

    def __mul__(self, other):
        ans = Expression()
        for elem1 in self:
            for elem2 in other:
                ans.add(elem1 + elem2)
        return ans


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = [[Expression()]]
        for ch in expression:
            if ch.isalpha():
                if not stack[-1][-1]:
                    stack[-1][-1] = Expression((ch,))
                else:
                    stack[-1][-1] = stack[-1][-1] * Expression((ch,))
            else:
                if ch == "{":
                    stack.append([Expression()])
                elif ch == ",":
                    stack[-1].append(Expression())
                elif ch == "}":
                    now_exp = Expression()
                    for exp in stack.pop():
                        now_exp = now_exp + exp
                    if not stack[-1][-1]:
                        stack[-1][-1] = now_exp
                    else:
                        stack[-1][-1] = stack[-1][-1] * now_exp
            # print(ch, "->", stack)
        return sorted(list(stack[0][0]))
```