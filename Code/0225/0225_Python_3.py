from queue import Queue


class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.put(x)
        for _ in range(self.queue.qsize() - 1):  # 将栈顶元素移动到队头位置
            self.queue.put(self.queue.get())

    def pop(self) -> int:
        return self.queue.get()

    def top(self) -> int:
        ans = self.queue.get()
        self.push(ans)
        return ans

    def empty(self) -> bool:
        return self.queue.empty()


if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print(obj.top())
    print(obj.pop())
    obj.empty()
