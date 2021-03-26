# 字符串
# O(1)


class Solution:
    def reformatDate(self, date: str) -> str:
        month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        day, month, year = date.split(" ")
        day = "".join([ch for ch in day if ch.isnumeric()])
        month = month_list.index(month) + 1

        return "-".join([year.zfill(4), str(month).zfill(2), str(day).zfill(2)])


if __name__ == "__main__":
    print(Solution().reformatDate("20th Oct 2052"))  # "2052-10-20"
    print(Solution().reformatDate("6th Jun 1933"))  # "1933-06-06"
    print(Solution().reformatDate("26th May 1960"))  # "1960-05-26"
