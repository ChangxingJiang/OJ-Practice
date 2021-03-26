class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1 and K == 1:
            return 0
        elif K % 2 == 0:
            return 1 if not self.kthGrammar(N - 1, K // 2) else 0
        else:
            return 1 if self.kthGrammar(N - 1, K // 2 + 1) else 0


if __name__ == "__main__":
    print(Solution().kthGrammar(1, 1))  # 0
    print(Solution().kthGrammar(2, 1))  # 0
    print(Solution().kthGrammar(2, 2))  # 1
    print(Solution().kthGrammar(3, 2))  # 1
    print(Solution().kthGrammar(4, 5))  # 1
