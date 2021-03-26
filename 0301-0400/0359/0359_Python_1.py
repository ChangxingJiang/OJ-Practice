class Logger:

    def __init__(self):
        self.log = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.log or timestamp - self.log[message] >= 10:
            self.log[message] = timestamp
            return True
        else:
            return False


if __name__ == "__main__":
    obj = Logger()
    print(obj.shouldPrintMessage(1, "foo"))  # True
    print(obj.shouldPrintMessage(2, "bar"))  # True
    print(obj.shouldPrintMessage(3, "foo"))  # False
    print(obj.shouldPrintMessage(8, "bar"))  # False
    print(obj.shouldPrintMessage(10, "foo"))  # False
    print(obj.shouldPrintMessage(11, "foo"))  # True
