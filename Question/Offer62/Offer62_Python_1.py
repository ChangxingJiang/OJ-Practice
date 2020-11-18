class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # 处理n==0的情况
        if n == 0:
            return 0

        # 处理n>0的情况
        else:
            return (self.lastRemaining(n - 1, m) + m) % n


if __name__ == "__main__":
    print(Solution().lastRemaining(2, 3))  # 1
    print(Solution().lastRemaining(5, 3))  # 3
    print(Solution().lastRemaining(10, 17))  # 2
