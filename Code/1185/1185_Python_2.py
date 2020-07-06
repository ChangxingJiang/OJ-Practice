class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        if month == 1 or month == 2:
            month += 12
            year -= 1
        ans = int((year + year // 4 - year // 100 + year // 400 + 2 * month + 3 * (month + 1) / 5 + day) % 7)
        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][ans]


if __name__ == "__main__":
    print(Solution().dayOfTheWeek(day=6, month=7, year=2020))  # Monday
    print(Solution().dayOfTheWeek(day=31, month=8, year=2019))  # Saturday
    print(Solution().dayOfTheWeek(day=29, month=2, year=2016))  # Monday
    print(Solution().dayOfTheWeek(day=18, month=7, year=1999))  # Sunday
    print(Solution().dayOfTheWeek(day=15, month=8, year=1993))  # Sunday
