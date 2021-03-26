import bisect
import collections


class TimeMap:

    def __init__(self):
        self.hashmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if len(self.hashmap[key]) > 0:
            i = bisect.bisect(self.hashmap[key], (timestamp, chr(127)))
            return self.hashmap[key][i - 1][1] if i - 1 >= 0 else ""
        else:
            return ""


if __name__ == "__main__":
    obj = TimeMap()
    obj.set("foo", "bar", 1)
    print(obj.get("foo", 1))  # bar
    print(obj.get("foo", 3))  # bar
    obj.set("foo", "bar2", 4)
    print(obj.get("foo", 4))  # bar2
    print(obj.get("foo", 5))  # bar2
    print()

    obj = TimeMap()
    obj.set("love", "high", 10)
    obj.set("love", "low", 20)
    print(obj.get("love", 5))  # ""
    print(obj.get("love", 10))  # high
    print(obj.get("love", 15))  # high
    print(obj.get("love", 20))  # low
    print(obj.get("love", 25))  # low
