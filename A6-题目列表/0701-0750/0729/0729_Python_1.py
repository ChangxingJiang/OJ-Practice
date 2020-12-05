class MyCalendar:

    def __init__(self):
        pass

    def book(self, start: int, end: int) -> bool:
        pass


if __name__ == "__main__":
    obj = MyCalendar()
    print(obj.book(10, 20))  # True
    print(obj.book(15, 25))  # False
    print(obj.book(20, 30))  # True
