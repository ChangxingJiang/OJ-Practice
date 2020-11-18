class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.pool = {i for i in range(maxNumbers)}

    def get(self) -> int:
        if self.pool:
            return self.pool.pop()
        else:
            return -1

    def check(self, number: int) -> bool:
        return number in self.pool

    def release(self, number: int) -> None:
        self.pool.add(number)


if __name__ == "__main__":
    directory = PhoneDirectory(3)
    print(directory.get())  # 0
    print(directory.get())  # 1
    print(directory.check(2))  # True
    print(directory.get())  # 2
    print(directory.check(2))  # False
    directory.release(2)
    print(directory.check(2))  # True
