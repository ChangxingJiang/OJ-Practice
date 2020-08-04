class Solution:
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


if __name__ == "__main__":
    print(Solution().calculate("1 + 1"))  # 2
    print(Solution().calculate(" 2-1 + 2 "))  # 3
    print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))  # 23
    print(Solution().calculate("2147483647"))  # 2147483647
    print(Solution().calculate("2-(5-6)"))  # 3
    print(Solution().calculate("2-4-(8+2-6+(8+4-(1)+8-10))"))  # -15
