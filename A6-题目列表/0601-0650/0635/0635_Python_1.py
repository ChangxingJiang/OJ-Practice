from typing import List


class LogSystem:

    def __init__(self):
        pass

    def put(self, id: int, timestamp: str) -> None:
        pass

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        pass


if __name__ == "__main__":
    obj = LogSystem()
    obj.put(1, "2017:01:01:23:59:59")
    obj.put(2, "2017:01:01:22:59:59")
    obj.put(3, "2016:01:01:00:00:00")
    print(obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"))  # [3,2,1]
    print(obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"))  # [2,1]
