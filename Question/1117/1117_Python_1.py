import threading


class H2O:
    def __init__(self):
        self.count = 0
        self.s1 = threading.Semaphore(2)
        self.s2 = threading.Semaphore(0)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.s1.acquire()
        releaseHydrogen()
        self.count += 1
        if self.count == 2:
            self.s2.release()
            self.count = 0

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.s2.acquire()
        releaseOxygen()
        self.s1.release()
        self.s1.release()


if __name__ == "__main__":
    pass
