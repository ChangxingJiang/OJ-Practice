class ProductOfNumbers:

    def __init__(self):
        pass

    def add(self, num: int) -> None:
        pass

    def getProduct(self, k: int) -> int:
        pass


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
