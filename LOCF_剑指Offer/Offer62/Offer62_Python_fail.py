class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # 处理m大于n的情况
        if m > n:
            val = self.lastRemaining(n, m % n)
            print(n, ",", m, "=", val)
            return val

        # 处理n=2的情况
        if n == 2:
            return m % 2

        # 处理n>2的情况
        val = (self.lastRemaining(n - 1, m) - n % m) % n
        print(n, ",", m, "=", val)
        return val


if __name__ == "__main__":
    print(Solution().lastRemaining(2, 3))  # 1
    print(Solution().lastRemaining(5, 3))  # 3
    print(Solution().lastRemaining(10, 17))  # 2
