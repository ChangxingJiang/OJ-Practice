class MyCalendarTwo:

    def __init__(self):
        self.lst1 = []
        self.lst2 = []

    def book(self, start: int, end: int) -> bool:
        for l, r in self.lst2:
            if max(start, l) < min(end, r):
                return False
        for l, r in self.lst1:
            t1, t2 = max(start, l), min(end, r)
            if t1 < t2:
                self.lst2.append([t1, t2])
        self.lst1.append([start, end])
        return True


if __name__ == "__main__":
    obj = MyCalendarTwo()
    print(obj.book(10, 20))  # True
    print(obj.book(50, 60))  # True
    print(obj.book(10, 40))  # True
    print(obj.book(5, 15))  # False
    print(obj.book(5, 10))  # True
    print(obj.book(25, 55))  # True
