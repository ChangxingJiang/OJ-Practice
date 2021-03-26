class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 9 + self.countNumbersWithUniqueDigits(0)
        else:
            res = 9 * 9
            for i in range(2, n):
                res *= (10 - i)
            return res + self.countNumbersWithUniqueDigits(n - 1)


if __name__ == "__main__":
    print(Solution().countNumbersWithUniqueDigits(2))  # 91
    print(Solution().countNumbersWithUniqueDigits(3))  # 739
