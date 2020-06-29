from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        pass


if __name__ == "__main__":
    e1 = Employee(1, 5, [2, 3])
    e2 = Employee(2, 3, [])
    e3 = Employee(3, 3, [])
    print(Solution().getImportance([e1, e2, e3], 1))  # 11
