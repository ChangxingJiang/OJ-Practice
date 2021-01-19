class Solution:
    def clumsy(self, N: int) -> int:
        if N <= 4:
            return [1, 2, 6, 7][N - 1]
        else:
            return N + [1, 2, 2, -1][N % 4]


if __name__ == "__main__":
    print(Solution().clumsy(4))  # 7
    print(Solution().clumsy(10))  # 12
