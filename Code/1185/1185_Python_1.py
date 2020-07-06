class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        ans = 4

        # 累加年份
        for y in range(1971, year):
            if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
                ans += 2
            else:
                ans += 1
        ans = ans % 7

        print(year, ans)

        # 累加月份
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            months[1] = 29
        ans += sum(months[:month - 1])
        ans = ans % 7

        print(year, ans)

        # 累加日期
        ans += day - 1

        print(year, ans)

        # 计算星期
        ans = ans % 7
        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][ans]


if __name__ == "__main__":
    print(Solution().dayOfTheWeek(day=6, month=7, year=2020))  # Monday
    print(Solution().dayOfTheWeek(day=31, month=8, year=2019))  # Saturday
    print(Solution().dayOfTheWeek(day=29, month=2, year=2016))  # Monday
    print(Solution().dayOfTheWeek(day=18, month=7, year=1999))  # Sunday
    print(Solution().dayOfTheWeek(day=15, month=8, year=1993))  # Sunday
