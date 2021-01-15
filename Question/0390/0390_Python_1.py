class Solution:
    def lastRemaining(self, n: int, reverse=False) -> int:
        if n == 1:
            return 1
        if not reverse:
            return self.lastRemaining(n // 2, not reverse) * 2
        else:
            if n % 2 == 0:
                return self.lastRemaining(n // 2, not reverse) * 2 - 1
            else:
                return self.lastRemaining(n // 2, not reverse) * 2


if __name__ == "__main__":
    print(Solution().lastRemaining(9))  # 6
