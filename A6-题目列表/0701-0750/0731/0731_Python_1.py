class MyCalendarTwo:

    def __init__(self):
        pass

    def book(self, start: int, end: int) -> bool:
        pass


if __name__ == "__main__":
    obj = MyCalendarTwo()
    print(obj.book(10, 20))  # True
    print(obj.book(50, 60))  # True
    print(obj.book(10, 40))  # True
    print(obj.book(5, 15))  # False
    print(obj.book(5, 20))  # True
    print(obj.book(25, 55))  # True
