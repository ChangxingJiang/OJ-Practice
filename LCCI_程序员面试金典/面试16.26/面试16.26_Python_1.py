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


if __name__ == "__main__":
    print(Solution().calculate("3+2*2"))  # 7
    print(Solution().calculate(" 3/2 "))  # 1
    print(Solution().calculate(" 3+5 / 2 "))  # 5
