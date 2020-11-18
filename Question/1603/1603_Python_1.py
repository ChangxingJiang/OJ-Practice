# 设计
# O(1)

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            self.big -= 1
            return self.big >= 0
        if carType == 2:
            self.medium -= 1
            return self.medium >= 0
        if carType == 3:
            self.small -= 1
            return self.small >= 0


if __name__ == "__main__":
    park = ParkingSystem(1, 1, 0)
    park.addCar(1)  # True
    park.addCar(2)  # True
    park.addCar(3)  # True
    park.addCar(1)  # False
