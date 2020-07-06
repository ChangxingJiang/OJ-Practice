class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 > date2:
            date1, date2 = date2, date1
        y1, m1, d1 = date1.split("-")
        y1, m1, d1 = int(y1), int(m1), int(d1)
        y2, m2, d2 = date2.split("-")
        y2, m2, d2 = int(y2), int(m2), int(d2)

        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        ans = 0

        # 统计整年
        for y in range(y1 + 1, y2):
            if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
                ans += 366
            else:
                ans += 365

        # 统计整月
        months1 = months_leap if y1 % 4 == 0 and (y1 % 100 != 0 or y1 % 400 == 0) else months
        months2 = months_leap if y2 % 4 == 0 and (y2 % 100 != 0 or y2 % 400 == 0) else months
        if y1 != y2:
            ans += sum(months1[m1:])
            ans += sum(months2[:m2 - 1])

        # 统计剩下的日期
        if y1 != y2 or m1 != m2:
            ans += months1[m1 - 1] - d1
            ans += d2
        else:
            ans += d2 - d1

        return ans


if __name__ == "__main__":
    print(Solution().daysBetweenDates(date1="2019-06-29", date2="2019-06-30"))  # 1
    print(Solution().daysBetweenDates(date1="2018-06-29", date2="2019-06-30"))  # 366
    print(Solution().daysBetweenDates(date1="2020-01-15", date2="2019-12-31"))  # 15
