class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        val = 0
        for i in range(1, n + 1):
            val = (val + m) % i
        return val


if __name__ == "__main__":
    print(Solution().lastRemaining(2, 3))  # 1
    print(Solution().lastRemaining(5, 3))  # 3
    print(Solution().lastRemaining(10, 17))  # 2
