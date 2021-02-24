class ProductOfNumbers:

    def __init__(self):
        self.array = [0]
        self.zero = 0

    def add(self, num: int) -> None:
        if num != 0:
            if self.array[-1] == 0:
                self.array.append(num)
            else:
                self.array.append(self.array[-1] * num)
        else:
            self.zero = len(self.array)
            self.array.append(0)

    def getProduct(self, k: int) -> int:
        idx2 = len(self.array) - 1
        idx1 = idx2 - k
        if idx1 < self.zero:
            return 0
        elif idx1 == self.zero:
            return self.array[idx2]
        else:
            return self.array[idx2] // self.array[idx1]


if __name__ == "__main__":
    obj = ProductOfNumbers()
    obj.add(3)
    obj.add(0)
    obj.add(2)
    obj.add(5)
    obj.add(4)
    print(obj.getProduct(2))  # 20
    print(obj.getProduct(3))  # 40
    print(obj.getProduct(4))  # 0
    obj.add(8)
    print(obj.getProduct(2))  # 32
