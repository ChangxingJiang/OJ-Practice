class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return pow(num, 0.5) % 1 == 0


if __name__ == "__main__":
    print(Solution().isPerfectSquare(16))  # True
    print(Solution().isPerfectSquare(14))  # False
