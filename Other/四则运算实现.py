class Solution:
    def calculate(self, s: str) -> int:
        # 清除无意义的空格
        s = s.replace(" ", "")

        # 合并连续的数字
        expresion = []
        now = ""
        for ch in s:
            if ch not in ["+", "-", "(", ")"]:
                now += ch
            else:
                if now:
                    expresion.append(now)
                    now = ""
                expresion.append(ch)
        if now:
            expresion.append(now)

        print(expresion)

        # 生成逆波兰表达式
        stack = []  # 符号栈
        tokens = []  # 逆波兰表达式(后缀表达式)
        for ch in expresion:
            if ch == "+":
                if stack and stack[-1] == "-":
                    tokens.append(stack.pop())
                stack.append(ch)
            elif ch == "-":
                if stack and stack[-1] == "-":
                    tokens.append(stack.pop())
                stack.append(ch)
            elif ch == "(":
                stack.append(ch)
            elif ch == ")":
                while stack:
                    top = stack.pop()
                    if top != "(":
                        tokens.append(top)
            else:
                tokens.append(ch)
        while stack:
            tokens.append(stack.pop())

        print(tokens)

        # 计算逆波兰表达式
        stack = []
        for token in tokens:
            if token == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            else:
                stack.append(int(token))
            print(stack)

        return stack[0]


if __name__ == "__main__":
    print(Solution().calculate("1 + 1"))  # 2
    print(Solution().calculate(" 2-1 + 2 "))  # 3
    print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))  # 23
    print(Solution().calculate("2147483647"))  # 2147483647
    print(Solution().calculate("2-(5-6)"))  # 3
    print(Solution().calculate("2-4-(8+2-6+(8+4-(1)+8-10))"))  # -15
