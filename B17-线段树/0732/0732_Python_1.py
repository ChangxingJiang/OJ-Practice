class MyCalendarThree:

    def __init__(self):
        pass

    def book(self, start: int, end: int) -> int:
        pass


if __name__ == "__main__":
    obj = MyCalendarThree()
    print(obj.book(10, 20))  # 1
    print(obj.book(50, 60))  # 1
    print(obj.book(10, 40))  # 2
    print(obj.book(5, 15))  # 3
    print(obj.book(5, 10))  # 3
    print(obj.book(25, 55))  # 3
