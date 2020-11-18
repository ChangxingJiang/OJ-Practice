class StreamRank:

    def __init__(self):
        pass

    def track(self, x: int) -> None:
        pass

    def getRankOfNumber(self, x: int) -> int:
        pass


if __name__ == "__main__":
    s = StreamRank()
    print(s.getRankOfNumber(1))  # 0
    s.track(0)
    print(s.getRankOfNumber(0))  # 1
