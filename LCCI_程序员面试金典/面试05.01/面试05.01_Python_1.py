class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        p1 = N >> (j + 1) << (j + 1)  # j位之后
        p2 = M << i  # i位到j位之间
        p3 = N & (2 ** i - 1)  # i位之前
        return p1 + p2 + p3


if __name__ == "__main__":
    print(Solution().insertBits(N=1024, M=19, i=2, j=6))  # 1100
    print(Solution().insertBits(N=0, M=31, i=0, j=4))  # 31
