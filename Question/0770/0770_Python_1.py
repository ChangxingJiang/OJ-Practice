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

        # print(expression, eval_hash)

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
            # print(i - 1, ":", expression[i - 1], "->", stack_poly, stack_symbol)
        else:
            token = expression[i_start:i]
            if token.isalpha() or token.isdigit():  # 处理当前项为数字的情况
                if token in eval_hash:
                    token = eval_hash[token]
                stack_poly.append(Polymerization(token))
                count(stack_symbol.pop())
            count(stack_symbol.pop())
        # print(i - 1, ":", expression[i - 1], "->", stack_poly, stack_symbol)

        final = stack_poly[0]
        ans = []
        for key in sorted(final, key=lambda x: (-len(x), x)):
            if final[key] != 0:
                ans.append("*".join([str(final[key])] + [str(k) for k in key]))
        return ans


if __name__ == "__main__":
    print(Solution().basicCalculatorIV(expression="e + 8 - a + 5", evalvars=["e"], evalints=[1]))  # ["-1*a","14"]
    print(Solution().basicCalculatorIV(expression="a + b", evalvars=["a", "b"], evalints=[10, -7]))  # ["3"]
    print(Solution().basicCalculatorIV(expression="e - 8 + temperature - pressure",
                                       evalvars=["e", "temperature"], evalints=[1, 12]))  # ["-1*pressure","5"]
    print(Solution().basicCalculatorIV(expression="(e + 8) * (e - 8)", evalvars=[], evalints=[]))  # ["1*e*e","-64"]
    print(Solution().basicCalculatorIV(expression="7 - 7", evalvars=[], evalints=[]))  # []
    print(Solution().basicCalculatorIV(expression="a * b * c + b * a * c * 4", evalvars=[], evalints=[]))  # ["5*a*b*c"]
    print(
        Solution().basicCalculatorIV(expression="((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))",
                                     evalvars=[],
                                     evalints=[]))  # ["-1*a*a*b*b","2*a*a*b*c","-1*a*a*c*c","1*a*b*b*b","-1*a*b*b*c","-1*a*b*c*c","1*a*c*c*c","-1*b*b*b*c","2*b*b*c*c","-1*b*c*c*c","2*a*a*b","-2*a*a*c","-2*a*b*b","2*a*c*c","1*b*b*b","-1*b*b*c","1*b*c*c","-1*c*c*c","-1*a*a","1*a*b","1*a*c","-1*b*c"]

    # 测试多项式类的加法、减法、乘法运算
    # poly1 = Polymerization("a")
    # poly2 = Polymerization("b")
    # poly3 = Polymerization("c")
    # print(poly1 * poly2 * poly3)

    # 测试多项式的构造方法
    # poly = Polymerization("pressure")
    # print(poly)
