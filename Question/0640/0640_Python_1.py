class Solution:
    def solveEquation(self, equation: str) -> str:
        def count(ss):
            aa, bb = 0, 0
            flag = 1 if ss[0] == "+" else -1
            if "x" in ss:
                s = now[1:].replace("x", "")
                aa = flag * (int(s) if s else 1)
            else:
                bb = flag * int(ss[1:])
            return aa, bb

        equation1, equation2 = equation.split("=")
        if equation1[0] != "-" and equation1[0] != "+":
            equation1 = "+" + equation1
        if equation2[0] != "-" and equation2[0] != "+":
            equation2 = "+" + equation2

        a, b = 0, 0

        # 计算等号左边
        now = ""
        for ch in equation1:
            if ch == "+" or ch == "-":
                if now:
                    c, d = count(now)
                    a += c
                    b += d
                now = ch
            else:
                now += ch
        c, d = count(now)
        a += c
        b += d

        # 计算等号右边
        now = ""
        for ch in equation2:
            if ch == "+" or ch == "-":
                if now:
                    c, d = count(now)
                    a -= c
                    b -= d
                now = ch
            else:
                now += ch
        c, d = count(now)
        a -= c
        b -= d

        # 计算结果
        if a == 0:
            if b == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x=" + str(-b // a)


if __name__ == "__main__":
    print(Solution().solveEquation("x+5-3+x=6+x-2"))  # "x=2"
    print(Solution().solveEquation("x=x"))  # "Infinite solutions"
    print(Solution().solveEquation("2x=x"))  # "x=0"
    print(Solution().solveEquation("2x+3x-6x=x+2"))  # "x=-1"
    print(Solution().solveEquation("x=x+2"))  # "No solution"
