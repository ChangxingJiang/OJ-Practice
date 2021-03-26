class Solution:
    def baseNeg2(self, N: int) -> str:
        now = 1
        ans = []
        while N:
            if now > 0:
                if N & (-N) == now:
                    N -= now
                    ans.append("1")
                else:
                    ans.append("0")
            else:
                if N & (-N) == -now:
                    N -= now
                    ans.append("1")
                else:
                    ans.append("0")
            now *= (-2)

        return "".join(ans[::-1]) if ans else "0"


if __name__ == "__main__":
    print(Solution().baseNeg2(0))  # "0"
    print(Solution().baseNeg2(2))  # "110"
    print(Solution().baseNeg2(3))  # "111"
    print(Solution().baseNeg2(4))  # "100"
