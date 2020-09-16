class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        half = int(pow(c, 0.5) + 1)
        for i in range(0, half):
            if pow(c - pow(i, 2), 0.5) % 1 == 0:
                return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().judgeSquareSum(5))  # True
    print(Solution().judgeSquareSum(3))  # False
    print(Solution().judgeSquareSum(0))  # True
