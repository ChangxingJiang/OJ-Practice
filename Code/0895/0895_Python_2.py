import collections


class FreqStack:
    def __init__(self):
        self.count = collections.Counter()
        self.stack = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, x: int) -> None:
        self.count[x] += 1
        self.max_freq = max(self.max_freq, self.count[x])
        self.stack[self.count[x]].append(x)

    def pop(self) -> int:
        ans = self.stack[self.max_freq].pop()
        if len(self.stack[self.max_freq]) == 0:
            self.max_freq -= 1
        self.count[ans] -= 1
        return ans


if __name__ == "__main__":
    obj = FreqStack()
    obj.push(5)
    obj.push(7)
    obj.push(5)
    obj.push(7)
    obj.push(4)
    obj.push(5)
    print(obj.pop())  # 5
    print(obj.pop())  # 7
    print(obj.pop())  # 5
    print(obj.pop())  # 4
