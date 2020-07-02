import collections


class RecentCounter:

    def __init__(self):
        self.queue = collections.deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)


if __name__ == "__main__":
    obj = RecentCounter()
    print(obj.ping(1))  # 1
    print(obj.ping(100))  # 2
    print(obj.ping(3001))  # 3
    print(obj.ping(3002))  # 3
