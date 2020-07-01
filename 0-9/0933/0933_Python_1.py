class RecentCounter:

    def __init__(self):
        pass

    def ping(self, t: int) -> int:
        pass


if __name__ == "__main__":
    obj = RecentCounter()
    print(obj.ping(1))  # 1
    print(obj.ping(100))  # 2
    print(obj.ping(3001))  # 3
    print(obj.ping(3002))  # 3
