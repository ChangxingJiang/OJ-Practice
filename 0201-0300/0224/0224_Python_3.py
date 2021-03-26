class Solution:
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


if __name__ == "__main__":
    print(Solution().calculate("1 + 1"))  # 2
    print(Solution().calculate(" 2-1 + 2 "))  # 3
    print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))  # 23
    print(Solution().calculate("2147483647"))  # 2147483647
    print(Solution().calculate("2-(5-6)"))  # 3
    print(Solution().calculate("2-4-(8+2-6+(8+4-(1)+8-10))"))  # -15
