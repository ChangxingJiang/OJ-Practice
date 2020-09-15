class Solution:
    def numWays(self, n: int) -> int:
        a = 1
        b = 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b % 1000000007


if __name__ == "__main__":
    print(Solution().numWays(2))  # 2
    print(Solution().numWays(7))  # 21
    print(Solution().numWays(0))  # 1
    print(Solution().numWays(1))  # 1
