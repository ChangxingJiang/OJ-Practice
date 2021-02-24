class Solution:
    def maximumTime(self, time: str) -> str:
        hour, minute = time.split(":")

        if time[0] == "?" and time[1] == "?":
            hour = "23"
        elif hour[0] == "?":
            if int(hour[1]) <= 3:
                hour = "2" + hour[1]
            else:  # int(hour[1]) > 3
                hour = "1" + hour[1]
        elif hour[1] == "?":
            if int(hour[0]) < 2:
                hour = hour[0] + "9"
            else:
                hour = hour[0] + "3"

        if minute[0] == "?" and minute[1] == "?":
            minute = "59"
        elif minute[0] == "?":
            minute = "5" + minute[1]
        elif minute[1] == "?":
            minute = minute[0] + "9"

        return hour + ":" + minute


if __name__ == "__main__":
    print(Solution().maximumTime("2?:?0"))  # "23:50"
    print(Solution().maximumTime("0?:3?"))  # "09:39"
    print(Solution().maximumTime("1?:22"))  # "19:22"
