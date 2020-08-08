# LeetCode题解(0770)：基本计算器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/basic-calculator-iv/)（困难）

标签：类、正则表达式、字符串、递归、栈、哈希表

| 解法           | 时间复杂度                                    | 空间复杂度 | 执行用时      |
| -------------- | --------------------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(2^N+N×M)$ : N为表达式长度，M为求值映射长度 | $O(N)$     | 72ms (60.00%) |
| Ans 2 (Python) |                                               |            |               |
| Ans 3 (Python) |                                               |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（设计多项式类）：

```python
import collections
from typing import List


class Polymerization(collections.Counter):
    """多项式类"""

    def __init__(self, expression: str = None):
        """
        构造方法
        :param expression: 只能构造基本单项式（不能包括加法、减法、乘法、括号）
        """
        super().__init__()
        if expression:
            if expression.isalpha():
                self[tuple({expression})] = 1
            else:
                self[tuple()] = int(expression)

    def __add__(self, other):
        """返回加法操作"""
        ans = Polymerization()
        ans.update(self)
        ans.update(other)
        return ans

    def __sub__(self, other):
        """实现减法操作"""
        ans = Polymerization()
        ans.update(self)
        ans.update({k: -v for k, v in other.items()})
        return ans

    def __mul__(self, other):
        """实现乘法操作"""
        ans = Polymerization()
        for k1, v1 in self.items():
            for k2, v2 in other.items():
                key = tuple(sorted(k1 + k2))
                value = v1 * v2
                ans[key] += value
        return ans


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        def count(symbol):
            """执行加法、减法或乘法运算"""
            last_1 = stack_poly.pop()
            last_2 = stack_poly.pop()
            if symbol == "+":
                stack_poly.append(last_2 + last_1)
            elif symbol == "-":
                stack_poly.append(last_2 - last_1)
            elif symbol == "*":
                stack_poly.append(last_2 * last_1)

        # 将求值映射结果替换到表达式中
        eval_hash = {}
        for i in range(len(evalvars)):
            eval_hash[evalvars[i]] = str(evalints[i])

        # 解析表达式
        i = 0  # 当前遍历坐标
        i_start = 0  # 当前项开始坐标
        N = len(expression)
        stack_symbol = ["+", "+"]  # 符号栈
        stack_poly = [Polymerization(), Polymerization()]  # 多项式栈
        while i < N:
            if expression[i] == " ":
                token = expression[i_start:i]
                if token.isalpha() or token.isdigit():  # 处理当前项为数字的情况
                    if token in eval_hash:
                        token = eval_hash[token]
                    stack_poly.append(Polymerization(token))
                    count(stack_symbol.pop())
                elif token == "+" or token == "-":  # 处理当前项为加号或减号的情况
                    count(stack_symbol.pop())
                    stack_poly.append(Polymerization())
                    stack_symbol.append(token)
                    stack_symbol.append("+")
                elif token == "*":  # 处理当前项为乘号的情况
                    stack_symbol.append(token)
                i += 1
                i_start = i
            elif expression[i] == "(":
                stack_poly += [Polymerization(), Polymerization()]
                stack_symbol += ["+", "+"]
                i += 1
                i_start = i
            elif expression[i] == ")":
                token = expression[i_start:i]
                if token:
                    if token in eval_hash:
                        token = eval_hash[token]
                    stack_poly.append(Polymerization(token))
                    count(stack_symbol.pop())
                count(stack_symbol.pop())
                count(stack_symbol.pop())
                i += 1
                i_start = i
            else:
                i += 1
        else:
            token = expression[i_start:i]
            if token.isalpha() or token.isdigit():  # 处理当前项为数字的情况
                if token in eval_hash:
                    token = eval_hash[token]
                stack_poly.append(Polymerization(token))
                count(stack_symbol.pop())
            count(stack_symbol.pop())

        final = stack_poly[0]
        ans = []
        for key in sorted(final, key=lambda x: (-len(x), x)):
            if final[key] != 0:
                ans.append("*".join([str(final[key])] + [str(k) for k in key]))
        return ans
```