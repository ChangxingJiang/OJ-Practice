# LeetCode题解(面试16.26)：计算器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/calculator-lcci/)（中等）

标签：字符串、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 68ms (99.81%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def calculate(self, s: str) -> int:
        marks = {"+", "-", "*", "/"}
        stack = []  # 多项式栈
        now_num = ""  # 当前数字
        last_mark = "+"  # 上一个符号
        for ch in s + "+":  # 在结尾添加无意义的运算符，使最后一个数字可以被计算
            if ch.isdigit():
                now_num += ch
            elif ch in marks:
                num = int(now_num)
                if last_mark == "+":
                    stack.append(num)
                elif last_mark == "-":
                    stack.append(-num)
                elif last_mark == "*":
                    stack[-1] *= num
                else:
                    stack[-1] = int(stack[-1] / num)
                now_num = ""
                last_mark = ch

        return sum(stack)
```