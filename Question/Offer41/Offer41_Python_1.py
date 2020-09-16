import bisect


class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.arr, num)

    def findMedian(self) -> float:
        a = len(self.arr) // 2
        b = (len(self.arr) - 1) // 2
        return (self.arr[a] + self.arr[b]) / 2


if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())

    obj = MedianFinder()
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())
