import threading


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.lock = threading.Semaphore(1)
        self.s3 = threading.Semaphore(0)
        self.s5 = threading.Semaphore(0)
        self.s15 = threading.Semaphore(0)

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 != 0:
                self.s3.acquire()
                printFizz()
                self.lock.release()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 == 0:
                self.s5.acquire()
                printBuzz()
                self.lock.release()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 == 0:
                self.s15.acquire()
                printFizzBuzz(i)
                self.lock.release()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.lock.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.s15.release()
            elif i % 3 == 0:
                self.s3.release()
            elif i % 5 == 0:
                self.s5.release()
            else:
                printNumber(i)
                self.lock.release()

if __name__ == "__main__":
    pass
