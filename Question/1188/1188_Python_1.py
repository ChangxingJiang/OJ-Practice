import collections
import threading


class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.en = threading.Semaphore(capacity)
        self.de = threading.Semaphore(0)
        self.queue = collections.deque()
        self.n = 0

    def enqueue(self, element: int) -> None:
        self.n += 1
        self.en.acquire()
        self.queue.appendleft(element)
        self.de.release()

    def dequeue(self) -> int:
        self.n -= 1
        self.de.acquire()
        val = self.queue.pop()
        self.en.release()
        return val

    def size(self) -> int:
        return self.n


if __name__ == "__main__":
    pass
