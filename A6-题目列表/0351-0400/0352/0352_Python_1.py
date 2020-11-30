from typing import List


class SummaryRanges:

    def __init__(self):
        pass

    def addNum(self, val: int) -> None:
        pass

    def getIntervals(self) -> List[List[int]]:
        pass


if __name__ == "__main__":
    obj = SummaryRanges()
    obj.addNum(1)
    print(obj.getIntervals())  # [1, 1]
    obj.addNum(3)
    print(obj.getIntervals())  # [1, 1], [3, 3]
    obj.addNum(7)
    print(obj.getIntervals())  # [1, 1], [3, 3], [7, 7]
    obj.addNum(2)
    print(obj.getIntervals())  # [1, 3], [7, 7]
    obj.addNum(6)
    print(obj.getIntervals())  # [1, 3], [6, 7]
