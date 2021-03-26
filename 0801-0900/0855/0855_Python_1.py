import bisect


class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.students = []

    def seat(self) -> int:
        if not self.students:
            max_idx = 0
        else:
            max_idx, max_val = 0, self.students[0]
            for i, s in enumerate(self.students):
                if i > 0:
                    prev = self.students[i - 1]
                    distance = (s - prev) // 2
                    if distance > max_val:
                        max_idx, max_val = prev + distance, distance
            distance = self.n - 1 - self.students[-1]
            if distance > max_val:
                max_idx = self.n - 1
        bisect.insort_right(self.students, max_idx)
        return max_idx

    def leave(self, p: int) -> None:
        self.students.remove(p)


if __name__ == "__main__":
    obj = ExamRoom(10)
    print(obj.seat())  # 0
    print(obj.seat())  # 9
    print(obj.seat())  # 4
    print(obj.seat())  # 2
    obj.leave(4)
    print(obj.seat())  # 5
