class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            return (num - 1) % 9 + 1


if __name__ == "__main__":
    print(Solution().addDigits(38))  # 2
    print(Solution().addDigits(0))  # 2
