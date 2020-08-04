class Solution:
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


if __name__ == "__main__":
    print(Solution().calculate("1 + 1"))  # 2
    print(Solution().calculate(" 2-1 + 2 "))  # 3
    print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))  # 23
    print(Solution().calculate("2147483647"))  # 2147483647
    print(Solution().calculate("2-(5-6)"))  # 3
    print(Solution().calculate("2-4-(8+2-6+(8+4-(1)+8-10))"))  # -15
