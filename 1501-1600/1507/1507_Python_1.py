class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        month = str(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].index(month) + 1).zfill(2)
        return "-".join([year, month, day[:-2].zfill(2)])


if __name__ == "__main__":
    print(Solution().reformatDate(date="20th Oct 2052"))  # "2052-10-20"
    print(Solution().reformatDate(date="6th Jun 1933"))  # "1933-06-06"
    print(Solution().reformatDate(date="26th May 1960"))  # "1960-05-26"
