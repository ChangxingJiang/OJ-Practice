class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        if M in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif M in (4, 6, 9, 11):
            return 30
        elif Y % 4 == 0 and (Y % 100 != 0 or Y % 400 == 0):
            return 29
        else:
            return 28


if __name__ == "__main__":
    print(Solution().numberOfDays(1992, 7))  # 31
    print(Solution().numberOfDays(2000, 2))  # 29
    print(Solution().numberOfDays(1900, 2))  # 28
