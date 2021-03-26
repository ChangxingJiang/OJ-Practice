class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return 2 ** (len(bin(N)) - 2) - 1 - N


if __name__ == "__main__":
    print(Solution().bitwiseComplement(5))  # 2
    print(Solution().bitwiseComplement(7))  # 0
    print(Solution().bitwiseComplement(10))  # 5
