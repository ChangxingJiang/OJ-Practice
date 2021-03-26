import collections


class MaxQueue:

    def __init__(self):
        self.queue = collections.deque()  # 数据存储队列
        self.most_queue = collections.deque()  # 最大值队列

    def max_value(self) -> int:
        return self.most_queue[0] if self.most_queue else -1

    def push_back(self, value: int) -> None:
        while self.most_queue and self.most_queue[-1] < value:
            self.most_queue.pop()
        self.most_queue.append(value)
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        value = self.queue.popleft()
        if value == self.most_queue[0]:
            self.most_queue.popleft()
        return value


if __name__ == "__main__":
    obj = MaxQueue()
    obj.push_back(1)
    obj.push_back(2)
    print(obj.max_value())  # 2
    print(obj.pop_front())  # 1
    print(obj.max_value())  # 2

    obj = MaxQueue()
    print(obj.pop_front())  # -1
    print(obj.max_value())  # -1
