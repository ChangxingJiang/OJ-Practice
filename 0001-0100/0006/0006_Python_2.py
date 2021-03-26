class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 处理特殊情况
        if numRows == 1:
            return s

        N = len(s)
        L = numRows - 1
        now = 0
        orient = 1
        ans = [[] for _ in range(numRows)]
        for i in range(N):
            ans[now].append(s[i])
            now += orient
            if now == 0:
                orient = 1
            elif now == L:
                orient = -1
        return "".join(["".join(p) for p in ans])


if __name__ == "__main__":
    print(Solution().convert(s="LEETCODEISHIRING", numRows=3))  # "LCIRETOESIIGEDHN"
    print(Solution().convert(s="LEETCODEISHIRING", numRows=4))  # "LDREOEIIECIHNTSG"
    print(Solution().convert(s="A", numRows=1))  # "A"
