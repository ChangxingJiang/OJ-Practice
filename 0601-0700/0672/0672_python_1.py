class Solution:
    def flipLights(self, n: int, m: int) -> int:
        if n == 1:
            return 2 if m > 0 else 1
        if n == 2:
            return [1, 3][m] if m <= 1 else 4
        if n >= 3:
            return [1, 4, 7][m] if m <= 2 else 8


if __name__ == "__main__":
    print(Solution().flipLights(1, 1))  # 2
    print(Solution().flipLights(2, 1))  # 3
    print(Solution().flipLights(3, 1))  # 4
