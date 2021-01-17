class Solution:
    def __init__(self):
        self.N = 0
        self.ans = 0
        self.now = []

    def countArrangement(self, N: int) -> int:
        self.N = N
        self.now = [0] * (N + 1)
        self.dfs(1)
        return self.ans

    def dfs(self, i):
        if i == self.N + 1:
            self.ans += 1
        for j in range(1, self.N + 1):
            if self.now[j] == 0 and (i % j == 0 or j % i == 0):
                self.now[j] = i
                self.dfs(i + 1)
                self.now[j] = 0


if __name__ == "__main__":
    print(Solution().countArrangement(1))  # 1
    print(Solution().countArrangement(2))  # 2
    print(Solution().countArrangement(3))  # 3
    print(Solution().countArrangement(4))  # 8
    print(Solution().countArrangement(5))  # 10
    print(Solution().countArrangement(6))  # 36
