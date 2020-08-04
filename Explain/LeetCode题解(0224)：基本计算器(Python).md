# LeetCode题解(0224)：基本计算器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/basic-calculator/)（困难）

标签：栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 708ms (5.14%)  |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 700ms（5.14%)  |
| Ans 3 (Python) | $O(N)$     | $O(N)$     | 100ms (76.94%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（先整理连续的数字，再使用符号栈生成结果）：

```python
def calculate(self, s: str) -> int:
    # 清除无意义的空格
    s = s.replace(" ", "")

    # 合并连续的数字
    tokens = []
    now = ""
    for ch in s:
        if ch not in ["+", "-", "(", ")"]:
            now += ch
        else:
            if now:
                tokens.append(now)
                now = ""
            tokens.append(ch)
    if now:
        tokens.append(now)

    # 计算结果
    ans = 0
    stack = []  # 符号栈
    for token in tokens:
        if token == "+" or token == "-" or token == "(":
            stack.append(token)
        elif token == ")":
            stack.pop()  # 删除左括号
            if stack:
                stack.pop()  # 删除左括号前的符号
        else:
            num = int(token)
            if stack.count("-") % 2 == 0:
                ans += num
            else:
                ans -= num
            if stack and stack[-1] != "(":
                stack.pop()

    return ans
```

解法二（整理连续数字的同时生成结果）：

```python
def calculate(self, s: str) -> int:
    stack = []  # 符号栈
    ans = 0
    number = 0  # 当前正在合并的数字
    for ch in s:
        if ch.isdigit():
            number = number * 10 + int(ch)
        elif ch == "+" or ch == "-":
            if stack.count("-") % 2 == 0:
                ans += number
                number = 0
            else:
                ans -= number
                number = 0
            if stack and stack[-1] != "(":
                stack.pop()
            stack.append(ch)
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            if stack.count("-") % 2 == 0:
                ans += number
                number = 0
            else:
                ans -= number
                number = 0
            if stack and stack[-1] != "(":
                stack.pop()
            stack.pop()  # 删除左括号
            if stack:
                stack.pop()  # 删除左括号前的符号

    if stack.count("-") % 2 == 0:
        ans += number
    else:
        ans -= number

    return ans
```

解法三（括号正负性栈）：

```python
def calculate(self, s: str) -> int:
    stack = []  # 符号栈
    outer_sign = 1  # 当前括号层级的正负性
    sign = 1  # 当前正负性
    ans = 0
    number = 0  # 当前正在合并的数字
    for ch in s:
        if ch.isdigit():
            number = number * 10 + int(ch)
        elif ch == "+":
            ans += sign * number
            number = 0
            sign = outer_sign * 1
        elif ch == "-":
            ans += sign * number
            number = 0
            sign = outer_sign * (-1)
        elif ch == "(":
            stack.append(sign * outer_sign)
            outer_sign = sign
        elif ch == ")":
            ans += sign * number
            number = 0
            stack.pop()
            outer_sign = 1
            for s in stack:
                outer_sign *= s
    ans += sign * number
    return ans
```



