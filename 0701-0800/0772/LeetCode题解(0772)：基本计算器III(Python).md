# LeetCode题解(0772)：基本计算器III(Python)

题目：[原题链接](https://leetcode-cn.com/problems/basic-calculator-iii/)（困难）

标签：数学、栈、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 52ms (80.86%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（中缀表达式转后缀表达式计算）：

```python
class Solution:
    def calculate(self, s: str) -> int:
        sign_list = {"+", "-", "*", "/", "(", ")"}

        # 合并整数+过滤空格
        # 时间复杂度:O(N)
        lst1 = []
        now = ""
        for ch in s:
            if ch in sign_list:
                if now:
                    lst1.append(now)
                    now = ""
                lst1.append(ch)
            elif ch.isnumeric():
                now += ch
        if now:
            lst1.append(now)

        # print(" ".join(lst1))

        # 将中缀表达式转换为后缀表达式
        lst2 = []
        stack = []
        for e in lst1:
            if e.isnumeric():
                lst2.append(e)
            else:
                if e == ")":
                    while stack and stack[-1] != "(":
                        lst2.append(stack.pop())
                    stack.pop()
                elif e == "*" or e == "/":
                    while stack and stack[-1] in {"*", "/"}:
                        lst2.append(stack.pop())
                    stack.append(e)
                elif e == "+" or e == "-":
                    while stack and stack[-1] in {"+", "-", "*", "/"}:
                        lst2.append(stack.pop())
                    stack.append(e)
                else:  # e == "("
                    stack.append(e)
        while stack:
            lst2.append(stack.pop())

        # print(" ".join(lst2))

        # 后缀表达式计算结果
        stack = []
        for e in lst2:
            if e.isnumeric():
                stack.append(int(e))
            else:
                b = stack.pop()
                a = stack.pop()
                if e == "+":
                    stack.append(a + b)
                elif e == "-":
                    stack.append(a - b)
                elif e == "*":
                    stack.append(a * b)
                else:  # e = "/"
                    stack.append(a // b)
            # print(stack)

        return stack[0]
```