class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, date = date.split("-")
        year, month, date = int(year), int(month), int(date)

        leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        if leap:
            month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        return sum(month_days[:month - 1]) + date


if __name__ == "__main__":
    print(Solution().dayOfYear(date="2019-01-09"))  # 9
    print(Solution().dayOfYear(date="2019-02-10"))  # 41
    print(Solution().dayOfYear(date="2003-03-01"))  # 60
    print(Solution().dayOfYear(date="2004-03-01"))  # 61
