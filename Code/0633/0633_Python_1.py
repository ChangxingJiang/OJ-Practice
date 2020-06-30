class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        half = int(pow(c, 0.5) + 1)
        for i in range(half):
            for j in range(i, half):
                if pow(i, 2) + pow(j, 2) == c:
                    return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().judgeSquareSum(5))  # True
    print(Solution().judgeSquareSum(3))  # False
