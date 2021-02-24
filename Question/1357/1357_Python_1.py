from typing import List


class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.prices = {products[i]: prices[i] for i in range(len(products))}
        self.i = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.i += 1
        discount = self.discount if (self.i % self.n == 0) else 0

        res = 0
        for i in range(len(product)):
            res += amount[i] * self.prices[product[i]]
        return res - res * discount / 100


if __name__ == "__main__":
    obj = Cashier(3, 50, [1, 2, 3, 4, 5, 6, 7], [100, 200, 300, 400, 300, 200, 100])
    print(obj.getBill([1, 2], [1, 2]))  # 500.0
    print(obj.getBill([3, 7], [10, 10]))  # 4000.0
    print(obj.getBill([1, 2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1, 1, 1]))  # 800.0
    print(obj.getBill([4], [10]))  # 4000.0
    print(obj.getBill([7, 3], [10, 10]))  # 4000.0
    print(obj.getBill([7, 5, 3, 1, 6, 4, 2], [10, 10, 10, 9, 9, 9, 7]))  # 7350.0
    print(obj.getBill([2, 3, 5], [5, 3, 2]))  # 2500.0
