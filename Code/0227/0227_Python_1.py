class Solution:
    def calculate(self, s: str) -> int:
        mark_level = {"+": 0, "-": 0, "*": 1, "/": 1}  # 定义符号优先级

        # 合并多位数字
        group = []  # 合并数字组
        for ch in s:
            if ch.isdigit():
                if group and group[-1].isdigit():
                    group[-1] += ch
                else:
                    group.append(ch)
            else:
                group.append(ch)

        # 将中缀表达式转换为后缀表达式
        expression = []  # 表达式
        stack = []  # 符号栈
        for ch in group:
            if ch.isdigit():
                expression.append(ch)
            elif ch in mark_level:
                while stack and mark_level[stack[-1]] >= mark_level[ch]:
                    expression.append(stack.pop())
                stack.append(ch)
        while stack:
            expression.append(stack.pop())

        # 后缀表达式求值
        stack = []  # 数字栈
        for ch in expression:
            if ch.isdigit():
                stack.append(int(ch))
            else:
                b = stack.pop()
                a = stack.pop()
                if ch == "+":
                    stack.append(a + b)
                elif ch == "-":
                    stack.append(a - b)
                elif ch == "*":
                    stack.append(a * b)
                elif ch == "/":
                    stack.append(a // b)

        return stack[0]


if __name__ == "__main__":
    print(Solution().calculate("3+2*2"))  # 7
    print(Solution().calculate(" 3/2 "))  # 1
    print(Solution().calculate(" 3+5 / 2 "))  # 5
    print(Solution().calculate("42"))  # 5
