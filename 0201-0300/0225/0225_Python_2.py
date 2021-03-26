from queue import LifoQueue


class MyStack:

    def __init__(self):
        self.queue = LifoQueue()

    def push(self, x: int) -> None:
        self.queue.put(x)

    def pop(self) -> int:
        return self.queue.get()

    def top(self) -> int:
        x = self.queue.get()
        self.push(x)
        return x

    def empty(self) -> bool:
        return self.queue.empty()