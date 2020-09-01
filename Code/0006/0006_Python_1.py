class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 处理特殊情况
        if numRows == 1:
            return s

        N = len(s)
        L = numRows * 2 - 2
        ans = [[] for _ in range(numRows)]
        for i in range(N):
            now = i % L
            if now > L / 2:
                now = L - now
            ans[now].append(s[i])
        print(ans)
        return "".join(["".join(p) for p in ans])


if __name__ == "__main__":
    print(Solution().convert(s="LEETCODEISHIRING", numRows=3))  # "LCIRETOESIIGEDHN"
    print(Solution().convert(s="LEETCODEISHIRING", numRows=4))  # "LDREOEIIECIHNTSG"
    print(Solution().convert(s="A", numRows=1))  # "A"
