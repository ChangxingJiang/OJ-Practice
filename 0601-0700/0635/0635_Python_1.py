from typing import List

TIME_LENGTH = {
    "Year": 4,
    "Month": 7,
    "Day": 10,
    "Hour": 13,
    "Minute": 16,
    "Second": 19
}


class LogSystem:

    def __init__(self):
        self.logs = []

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        bits_num = TIME_LENGTH[granularity]

        ans = []
        for log in self.logs:
            if start[:bits_num] <= log[1][:bits_num] <= end[:bits_num]:
                ans.append(log[0])
        return ans


if __name__ == "__main__":
    obj = LogSystem()
    obj.put(1, "2017:01:01:23:59:59")
    obj.put(2, "2017:01:01:22:59:59")
    obj.put(3, "2016:01:01:00:00:00")
    print(obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"))  # [3,2,1]
    print(obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"))  # [2,1]
