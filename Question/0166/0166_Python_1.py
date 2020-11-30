class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 处理负数
        if numerator * denominator < 0:
            numerator *= -1
            sign = "-"
        else:
            sign = ""

        ans = []
        i2 = 0
        count = {}
        while True:
            if numerator not in count:
                count[numerator] = i2
                now, numerator = divmod(numerator, denominator)  # a=numerator//denominator; b=numerator%denominator
                ans.append(now)
                if numerator == 0:
                    if len(ans) == 1:
                        return sign + str(ans[0])
                    else:
                        return sign + "".join(str(ch) for ch in ([ans[0]] + ["."] + ans[1:]))
                else:
                    numerator *= 10
            else:
                i1 = count[numerator]
                return sign + "".join(str(ch) for ch in ([ans[0]] + ["."] + ans[1:i1] + ["("] + ans[i1:] + [")"]))
            i2 += 1


if __name__ == "__main__":
    # 0.5
    print(Solution().fractionToDecimal(1, 2))

    # 2
    print(Solution().fractionToDecimal(2, 1))

    # 0.(6)
    print(Solution().fractionToDecimal(2, 3))

    # 0.(012)
    print(Solution().fractionToDecimal(4, 333))

    # 0.2
    print(Solution().fractionToDecimal(1, 5))

    # 0.1(6)
    print(Solution().fractionToDecimal(1, 6))

    # 0
    print(Solution().fractionToDecimal(0, 3))

    # -6.25
    print(Solution().fractionToDecimal(-50, 8))

    # 11
    print(Solution().fractionToDecimal(-22, -2))
