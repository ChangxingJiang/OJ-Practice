class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        num = 0
        for i in range(1, n + 1):
            if n % i == 0:
                num += 1
                if num == k:
                    return i
        return -1


if __name__ == "__main__":
    print(Solution().kthFactor(12, 3))  # 3
    print(Solution().kthFactor(7, 2))  # 7
    print(Solution().kthFactor(4, 4))  # -1
    print(Solution().kthFactor(1, 1))  # 1
    print(Solution().kthFactor(1000, 3))  # 4
