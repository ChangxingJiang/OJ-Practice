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


if __name__ == "__main__":
    print(Solution().calculate("1 + 1"))  # 2
    print(Solution().calculate(" 6-4 / 2 "))  # 4
    print(Solution().calculate("2*(5+5*2)/3+(6/2+8)"))  # 21
    print(Solution().calculate("(2+6* 3+5- (3*14/7+2)*5)+3"))  # -12
    print(Solution().calculate("0"))  # 0
    print(Solution().calculate("1*2-3/4+5*6-7*8+9/10"))  # -24
