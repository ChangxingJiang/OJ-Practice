import collections


class FreqStack:
    def __init__(self):
        self.count = collections.Counter()
        self.stack = []

    def push(self, x: int) -> None:
        self.count[x] += 1
        self.stack.append(x)

    def pop(self) -> int:
        # 计算所有最频繁的元素
        most_common = self.count.most_common()
        maybe_ans = [most_common[0][0]]
        now_max = most_common[0][1]
        idx = 1
        while idx < len(most_common):
            if most_common[idx][1] == now_max:
                maybe_ans.append(most_common[idx][0])
                idx += 1
            else:
                break

        # 计算最靠近栈顶的元素
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] in maybe_ans:
                self.count[self.stack[i]] -= 1
                return self.stack.pop(i)


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
