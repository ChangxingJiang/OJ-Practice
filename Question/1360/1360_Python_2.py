import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 > date2:
            date1, date2 = date2, date1
        y1, m1, d1 = date1.split("-")
        y1, m1, d1 = int(y1), int(m1), int(d1)
        y2, m2, d2 = date2.split("-")
        y2, m2, d2 = int(y2), int(m2), int(d2)
        date1 = datetime.datetime(y1, m1, d1)
        date2 = datetime.datetime(y2, m2, d2)
        return (date2 - date1).days


if __name__ == "__main__":
    print(Solution().daysBetweenDates(date1="2019-06-29", date2="2019-06-30"))  # 1
    print(Solution().daysBetweenDates(date1="2018-06-29", date2="2019-06-30"))  # 366
    print(Solution().daysBetweenDates(date1="2020-01-15", date2="2019-12-31"))  # 15
