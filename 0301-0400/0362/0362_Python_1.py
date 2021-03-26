import collections


class HitCounter:

    def __init__(self):
        self.queue = collections.deque()

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.queue and self.queue[0] <= timestamp - 300:
            self.queue.popleft()
        return len(self.queue)


if __name__ == "__main__":
    obj = HitCounter()
    obj.hit(1)
    obj.hit(2)
    obj.hit(3)
    print(obj.getHits(4))  # 3
    obj.hit(300)
    print(obj.getHits(300))  # 4
    print(obj.getHits(301))  # 3
