class UndergroundSystem:

    def __init__(self):
        self.time_info = {}
        self.passenger = {}

    def checkIn(self, id: int, station1: str, t1: int) -> None:
        self.passenger[id] = [station1, t1]

    def checkOut(self, id: int, station2: str, t2: int) -> None:
        station1, t1 = self.passenger[id]
        if (station1, station2) not in self.time_info:
            self.time_info[(station1, station2)] = [0, 0]
        self.time_info[(station1, station2)][0] += t2 - t1
        self.time_info[(station1, station2)][1] += 1

    def getAverageTime(self, station1: str, station2: str) -> float:
        return self.time_info[(station1, station2)][0] / self.time_info[(station1, station2)][1]


if __name__ == "__main__":
    obj = UndergroundSystem()
    obj.checkIn(45, "Leyton", 3)
    obj.checkIn(32, "Paradise", 8)
    obj.checkIn(27, "Leyton", 10)
    obj.checkOut(45, "Waterloo", 15)
    obj.checkOut(27, "Waterloo", 20)
    obj.checkOut(32, "Cambridge", 22)
    print(obj.getAverageTime("Paradise", "Cambridge"))  # 14
    print(obj.getAverageTime("Leyton", "Waterloo"))  # 11
    obj.checkIn(10, "Leyton", 24)
    print(obj.getAverageTime("Leyton", "Waterloo"))  # 11
    obj.checkOut(10, "Waterloo", 38)
    print(obj.getAverageTime("Leyton", "Waterloo"))  # 12
