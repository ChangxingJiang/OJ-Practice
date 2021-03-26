class Leaderboard:

    def __init__(self):
        self.hashmap = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.hashmap:
            self.hashmap[playerId] = score
        else:
            self.hashmap[playerId] += score

    def top(self, K: int) -> int:
        return sum(sorted(self.hashmap.values(), reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        del self.hashmap[playerId]


if __name__ == "__main__":
    obj = Leaderboard()
    print(obj.addScore(1, 73))
    print(obj.addScore(2, 56))
    print(obj.addScore(3, 39))
    print(obj.addScore(4, 51))
    print(obj.addScore(5, 4))
    print(obj.top(1))  # 73
    print(obj.reset(1))
    print(obj.reset(2))
    print(obj.addScore(2, 51))
    print(obj.top(3))  # 141
