class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [int(t) for t in a]
        b = [int(t) for t in b]

        N1 = len(a)
        N2 = len(b)

        ans = []
        now = 0
        for i in range(1, max(N1, N2) + 1):
            # 计算当期数量
            c = now
            if i <= N1:
                c += a[-i]
            if i <= N2:
                c += b[-i]

            # 计算当前位及进位
            if c == 0:
                ans.append("0")
                now = 0
            elif c == 1:
                ans.append("1")
                now = 0
            elif c == 2:
                ans.append("0")
                now = 1
            else:
                ans.append("1")
                now = 1
        if now == 1:
            ans.append("1")
        return "".join(ans[::-1])


if __name__ == "__main__":
    print(Solution().addBinary("11", "1"))  # 100
    print(Solution().addBinary("1010", "1011"))  # 10101
