import sys

# 调整Python默认递归深度
sys.setrecursionlimit(100000)

class Solution:
    def sumNums(self, n: int) -> int:
        return n > 0 and n + self.sumNums(n - 1)


if __name__ == "__main__":
    print(Solution().sumNums(3))  # 6
    print(Solution().sumNums(9))  # 45
