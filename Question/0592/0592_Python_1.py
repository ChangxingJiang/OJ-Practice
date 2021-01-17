import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        def analyse(ss):
            if ss[0] == "+":
                flag = 1
            else:
                flag = -1
            s1, s2 = ss[1:].split("/")
            n1, n2 = int(s1), int(s2)
            return (flag, n1, n2)

        if expression[0] != "-":
            expression = "+" + expression

        lst = []
        now = ""
        for ch in expression:
            if ch == "+" or ch == "-":
                if now:
                    lst.append(analyse(now))
                now = ch
            else:
                now += ch
        lst.append(analyse(now))

        res1, res2 = 0, 2520
        for flag, n1, n2 in lst:
            res1 += flag * n1 * res2 // n2  # 1-10的最小公倍数=2520

        if res1 == 0:
            return "0/1"
        else:
            v = math.gcd(res1, res2)
            return str(res1 // v) + "/" + str(res2 // v)


if __name__ == "__main__":
    print(Solution().fractionAddition("-1/2+1/2"))  # "0/1"
    print(Solution().fractionAddition("-1/2+1/2+1/3"))  # "1/3"
    print(Solution().fractionAddition("1/3-1/2"))  # "-1/6"
    print(Solution().fractionAddition("5/3+1/3"))  # "2/1"
