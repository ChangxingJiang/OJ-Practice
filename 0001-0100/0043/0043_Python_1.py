class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 处理特殊情况
        if num1 == "0" or num2 == "0":
            return "0"

        N1 = len(num1)
        N2 = len(num2)
        N = N1 + N2

        # print("N1", "=", N1)
        # print("N2", "=", N2)

        ans = []
        step = 2
        now = 0
        while step <= N:
            # print(step, "->", max(step - N2, 1), min(step, N1 + 1))
            for i1 in range(max(step - N2, 1), min(step, N1 + 1)):
                i2 = step - i1
                # print(step, ":", i1, i2)
                now += int(num1[-i1]) * int(num2[-i2])
            ans.append(str(now % 10))
            now //= 10
            step += 1
        while now:
            ans.append(str(now % 10))
            now //= 10

        return "".join(ans[::-1])


if __name__ == "__main__":
    print(Solution().multiply(num1="2", num2="3"))  # 6
    print(Solution().multiply(num1="123", num2="456"))  # 56088
    print(Solution().multiply(num1="9", num2="99"))  # 891
    print(Solution().multiply(num1="99", num2="9"))  # 891
    print(Solution().multiply(num1="9133", num2="0"))  # 0
